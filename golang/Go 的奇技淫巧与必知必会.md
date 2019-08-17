# Go 的奇技淫巧与必知必会
## 1. go的全部类型与其zero value
| numbers(int...) | booleans(bool) | strings(string) | interface{} | reference types(slice, pointer, map, channel, function) | aggregate type(array, struct) |
| - | - | - | - | -| - |
| 0 | false | "" | nil | nil | zero value of all of its elements or fields |
---
## 2. 关于Channel必知必会的一些知识点
>   1. 有两种channel，a.不带缓冲的；b.带缓冲的；
>   2. 要理解chan的阻塞机制很简单，可以想象一个生产者一个消费者的情况，chan缓冲的大小，就是有多少个空槽（不带缓冲就是0个空槽）存储生产者生产的产品。send对应生产，receive对应消费
>   3. 对于不带缓冲的chan, send操作会阻塞，直到有receive操作（因为生产者生产的产品没地方放，只有等着消费者消费了，才能继续干活）；receive操作会阻塞，直到有send操作（生产者还没产品，消费者只能干等着）
>   4. 对于带缓冲的chan（缓冲大小为n），每一个send操作，会往槽里放一个产品，空槽的个数-1；每一个receive操作，会取走槽里的产品，空槽的个数+1。只有在空槽个数为0，然后send，或者槽里没产品（空槽个数为n）,然后receive时才会阻塞。因为当空槽个数为0时，生产者只有等有新的空槽，才能继续干活；或者消费者只有等有新的产品，才能继续消费。
>   5. 对于有缓冲的channel，往里面send的数据是存在一个FIFO的队列里面，也就意味着，我最先send的数据，最先被receive
>   6. 在一个已经close的chan上的receive会消费掉所有已send的数据（close之前的），在这之后的receive会立即返回当前chan类型的zero value。
>   7. 往已close的channel上send，会panic
>   8. 在nil的channel上面进行send，receive会永远阻塞,会造成对应协程goroutine leak

---

## 3. Channel 的常用的模式
1. ok
```go
v,ok := <-ch //如果ch已经关闭，ok返回false，否则true

```
2. range
```go
//当ch接受到数据时，才会执行下一个loop，并且当ch被close 掉之后，for循环会自动退出
for v := range ch{
    //do something...
}
```
3. 基于close的广播机制
    - eg1 利用chan的关闭来实现任务的取消
        ```go
        func TestCancel(t *testing.T) {
            cancelChan := make(chan struct{}, 0)
            for i := 0; i < 5; i++ {
                go func(i int, cancelCh chan struct{}) {
                    for {
                        if isCancelled(cancelCh) {
                            break
                        }
                        time.Sleep(time.Millisecond * 5)
                    }
                    fmt.Println(i, "Cancelled")
                }(i, cancelChan)
            }
            cancel2(cancelChan)
            time.Sleep(time.Second)

        }

        // cancel1  only one goroutine can be stopped
        func cancel1(cancelCh chan struct{}) {
            cancelCh <- struct{}{}
        }

        // cancel2   broadcast the channel closed
        func cancel2(cancelCh chan struct{}) {
            close(cancelCh)
        }
        func isCancelled(cancelCh chan struct{}) bool {
            select {
            case <-cancelCh:
                return true
            default:
                return false
            }
        } 
        ```
    - eg2 生产者消费者模型
        ```go
            func TestChannelClose(t *testing.T) {
                var wg sync.WaitGroup
                ch := make(chan int)
                wg.Add(1)
                dataProducer(ch, &wg)
                wg.Add(1)
                dataReceiver(ch, &wg)
                wg.Add(1)
                dataReceiver(ch, &wg)
                wg.Wait()

            }
        func dataProducer(ch chan int, wg *sync.WaitGroup) {
            go func() {
                for i := 0; i < 10; i++ {
                    ch <- i
                }
                // close just broadcast receivers 
                close(ch)
                wg.Done()
            }()

        }
        func dataReceiver(ch chan int, wg *sync.WaitGroup) {
            go func() {
                for {
                    if data, ok := <-ch; ok {
                        //t.Logf("%d\n", data)
                        fmt.Println(data)
                    } else {
                        break
                    }
                }
                wg.Done()
            }()
        }
        ```
    - eg3 仅需任一任务完成（多搜索器搜索，任意一个完成即可返回）
        ```go
        func runTask(i int) string {
	        return fmt.Sprintf("the response from %d\n", i)
        }
        func FirstResponse() string {
            numOfRunner := 10
            //ch := make(chan string)	// goroutine leak
            ch := make(chan string, 10)
            for i := 0; i < numOfRunner; i++ {
                go func(i int) {
                    ret := runTask(i)
                    ch <- ret
                }(i)
            }
            return <-ch
        }

        func TestFirstResponse(t *testing.T) {
            fmt.Println("before:", runtime.NumGoroutine())
            fmt.Println(FirstResponse())
            time.Sleep(time.Second)

            fmt.Println("After:", runtime.NumGoroutine())
        }
        ```
    - eg4 所有任务完成（可用WaitGroup）
        ```go
        func AllResponse() string {
            numOfRunner := 10
            //ch := make(chan string)	// goroutine leak
            ch := make(chan string, 10)
            for i := 0; i < numOfRunner; i++ {
                go func(i int) {
                    ret := runTask(i)
                    ch <- ret
                }(i)
            }
            finalRet := ""
            for j := 0; j < numOfRunner; j++ {
                finalRet += (<-ch + "\n")
            }
            return finalRet

        }

        func TestAllResponse(t *testing.T) {
            fmt.Println("before:", runtime.NumGoroutine())
            fmt.Println(AllResponse())
            time.Sleep(time.Second)

            fmt.Println("After:", runtime.NumGoroutine())
        }
4. limiting concurrency in Go
    ```golang
        //最大5个协程
        concurrency := 5
        sem := make(chan bool, concurrency)
        urls := []string{"url1", "url2"}
        for _, url := range urls {
            sem <- true
            go func(url) {
                defer func() { <-sem }()
                // get the url
            }(url)
        }
        for i := 0; i < cap(sem); i++ {
            sem <- true
        }
    ```
5. timeout
    ```golang
    func main() {

        c1 := make(chan string, 1)
        go func() {
            time.Sleep(2 * time.Second)
            c1 <- "result 1"
        }()

        select {
        case res := <-c1:
            fmt.Println(res)
        case <-time.After(1 * time.Second):
            fmt.Println("timeout 1")
        }
        c2 := make(chan string, 1)
        go func() {
            time.Sleep(2 * time.Second)
            c2 <- "result 2"
        }()
        select {
        case res := <-c2:
            fmt.Println(res)
        case <-time.After(3 * time.Second):
            fmt.Println("timeout 2")
        }
    }
    ```
---
## 4. sync 包的常见用法
1. Mutex
    - Mutex
    - RWMutex
2. WaitGroup
3. Context
    - eg1 任务的取消
        ```go
        func TestContext(t *testing.T) {
        ctx, cancel := context.WithCancel(context.Background())
        for i := 0; i < 5; i++ {
            go func(i int, ctx context.Context) {
                for {
                    if isCancelled2(ctx) {
                        break
                    }
                    time.Sleep(time.Millisecond * 5)
                }
                fmt.Println(i, "Cancelled")
            }(i, ctx)
        }
        cancel()
        time.Sleep(time.Second)

        }

        func isCancelled2(ctx context.Context) bool {
            select {
            case <-ctx.Done():
                return true
            default:
                return false
            }
        }
        ```
- Once
    - eg1   单例懒汉式
        ```go
        var once sync.Once

            var singleInstance *SingletonObj

            type SingletonObj struct {
            }

            func GetSingletonObj() *SingletonObj {
                //var res *SingletonObj
                once.Do(func() {
                    fmt.Println("Create Singleton obj.")
                    singleInstance = new(SingletonObj)
                })
                return singleInstance
            }

            func TestOnce(t *testing.T) {
                var wg sync.WaitGroup

                for i := 0; i < 10; i++ {
                    wg.Add(1)
                    go func() {
                        obj := GetSingletonObj()
                        fmt.Printf("%p\n", obj)
                        wg.Done()
                    }()
                }
                wg.Wait()
            }
            ```

- Pool  （对象缓存）
    - sync.Pool 的对象获取
        1. 尝试从私有对象获取
        2. 私有对象不存在，尝试从当前Processor的共享池获取
        3. 如果当前Processor共享池是空的，那么尝试从其它的Processor的共享池获取
        4. 如果所有共享池都是空的，最后就用用户指定的New函数产生一个新对象返回
    ![sync.Pool](./syncPool.jpg)
    - 对象的放回
        1. 如果私有对象不存在则保存为私有对象
        2. 如果私有对象存在，放入当前Processor共享池中
    - 对象的生命周期
        1. GC会清除sync.Pool缓存的对象
        2. 对象的缓存有效期为下一次GC之前
    - 总结
        1. 适用于通过复用，降低复杂对象的创建和GC代价
        2. 协程安全，会有锁的开销
        3. 生命周期受GC影响，不适合与做连接池等，需要自己管理生命周期的资源的池化

---

## 4. time 包的常见用法
1. Ticker
    - eg






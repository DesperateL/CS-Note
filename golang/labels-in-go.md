# Labels in go

## 总览
| |break|goto|continue|
|-|-|-|-|
|label必选|否|否|是|
|含义|跳出label下面的loop或者select、switch（必须紧接着label声明）|跳到label下面执行（label的声明可以在goto语句之后）|与break类似，不过是执行下一个iteration，并且只能用于loop|
---
## 1.关于label的知识
1. label的作用域是函数内，声明之前也可以调用。
    ```go
    func main() {
    fmt.Println(1)
    goto End
    fmt.Println(2)
    End:
    fmt.Println(3)
    }
    ```
    输出：
    ```
    1
    3
    ```
2. label作用域不包含嵌套函数
    ```go
    func() {
        fmt.Println(“Nested function”)
        goto End    //报错：label End not defined
    }()
    End:
    ```
3. label的作用域不是块作用域，所以不能在块中重新声明
    ```go
    goto X
    X:
    {
    X:  // already declared label.
    }
    ```
4. label的标识符与变量的标识符相互独立
    ```go
    x := 1
    goto x
    x:
    fmt.Println(x)
    ```
---
## 2.break语句（可选label）
go中break不仅可以结束最里面的for，switch还可以结束select。（在考虑终结select和switch的意义何在...）**特别注意，如果for里面包含switch或select，并且switch和select里面有break语句，那么break只能终结最里面的switch和select，并不能跳出for循环。**
### 知识点：
1. break不能跨越函数边界
    ```go
    func f() {
    break   //break is not in a loop
    }
    func main() {
        for i := 0; i < 10; i++ {
            f()
        }
    }
    ```
2. break label必须紧跟一个封闭的for、switch、select.
    ```go
    FirstLoop:  //invalid break label FirstLoop
    for i := 0; i < 10; i++ {
    }
    for i := 0; i < 10; i++ {
        break FirstLoop
    }
    ```
3. break label可以终结紧跟的for、switch、select.
    ```go
    OuterLoop:
    for i := 0; i < 10; i++ {
        for j := 0; j < 10; j++ {
            fmt.Printf(“i=%v, j=%v\n”, i, j)
            break OuterLoop     //可以直接跳出最外面的for循环
        }
    }
    ```
    输出
    ```go
    i=0, j=0
    ```
    对于外部的switch和select也是一样
    ```go
    SwitchStatement:
    switch 1 {
    case 1:
        fmt.Println(1)
        for i := 0; i < 10; i++ {
            break SwitchStatement
        }
        fmt.Println(2)
    }
    fmt.Println(3)
    ```
    输出：
    ```go
    1
    3
    ```
---
## 3.continue语句（可选label）
continue与break相似，但是是开始下一个loop，而且只用于loop。也就是说switch和select不能用。

```go
OuterLoop:
    for i := 0; i < 3; i++ {
        for j := 0; j < 3; j++ {
            fmt.Printf(“i=%v, j=%v\n”, i, j)
            continue OuterLoop
        }
    }
```
输出：
```go
i=0, j=0
i=1, j=0
i=2, j=0
```
---
## 4.goto语句（label必需）
goto语句用于跳转到label代码处
```go
i := 0
Start:
    fmt.Println(i)
    if i > 2 {
        goto End
    } else {
        i += 1
        goto Start
    }
End:
```
输出：
```go
0
1
2
3
```
### 注意：goto需要遵循两条规则
1. 变量声明不能被跳过
    ```go
    goto Done
    v := 0
    Done:   //goto Done jumps over declaration of v at…
    fmt.Println(v)
    ```
2. goto不能跳到其它块执行
    ```go
    goto Block
    {
    Block:  //goto Block jumps into block starting at …
        v := 0
        fmt.Println(v)
    }
    ```
## Reference
1. [Labels in Go - Michał Łowicki - medium-Aug 15, 2016](https://medium.com/golangspec/labels-in-go-4ffd81932339)
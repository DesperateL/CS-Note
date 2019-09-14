# The Law of Reflection

ref: [The Law of Reflection](https://blog.golang.org/laws-of-reflection)

## 前置知识：
### 静态类型(static type):每个变量都有一个静态类型，其静态类型在编译期间决定。
### 底层类型(underlying type):
```golang
type MyInt int

var i int
var j MyInt
```
i和j有不同的静态类型，尽管它们的底层类型相同。没有类型转换的化，它们不能相互赋值。

### interface的表示 [Go Data Structures: Interfaces](https://research.swtch.com/interfaces)
interface的变量底层储存着一个二元组（value,type）。
value：代表了底层具体的值
type：描述了interface的具体类型（转换之前的静态类型）
```golang
var r io.Reader
tty, err := os.OpenFile("/dev/tty", os.O_RDWR, 0)
if err != nil {
    return nil, err
}
r = tty
```
例如上面的例子中，r的二元组就表示为（tty,*os.File）
---
## 反射法则一：从接口对象到反射对象
refelct.Type : 可以通过reflect.TypeOf()方法获得接口二元组的type;
reflect.Value: 可以通过reflect.ValueOf()方法获得接口二元组的value.
Type和Value类型都有Kind()方法，这个方法可以返回值的底层类型，Uint, Float64, Slice, 等等。
Value类型还有Int(),Float()方法可以拿到反射对象存储的值。
通过SetInt()之类的方法可以改变反射对象存储的值，不过在使用此类方法之前，我们需要知道其是否是可设置的（settable）。

```golang
var x uint8 = 'x'
v := reflect.ValueOf(x)
fmt.Println("type:", v.Type())                            // uint8.
fmt.Println("kind is uint8: ", v.Kind() == reflect.Uint8) // true.
x = uint8(v.Uint())                                       // v.Uint returns a uint64.

```
---
## 反射法则二:从反射对象到接口值
通过Value类型的Interface()方法，我们可以得到反射值的interface表示。
```golang
y := v.Interface().(float64) // y will have type float64.
fmt.Println(y)
```
---
## 反射法则三:想要改变反射对象，那么其一定是可以设置的（settable）

因为有传值和传引用区分，所有想要改变反射对象，那么ValueOf()传进来的一定要是引用。
```golang
var x float64 = 3.4
p := reflect.ValueOf(&x) // Note: take the address of x.
fmt.Println("type of p:", p.Type()) //type of p: *float64
fmt.Println("settability of p:", p.CanSet()) //settability of p: false. the p isn't what we want to set, instead of *p.
v := p.Elem()   //To get to what p points to, we call the Elem method of Value
fmt.Println("settability of v:", v.CanSet())    //settability of v: true, Now v is a settable reflection object
v.SetFloat(7.1)
fmt.Println(v.Interface())  //7.1
fmt.Println(x)  //7.1
```
对于对象我们同样可以这样做
```golang
type T struct {
    A int
    B string
}
t := T{23, "skidoo"}
s := reflect.ValueOf(&t).Elem()
typeOfT := s.Type()
for i := 0; i < s.NumField(); i++ {
    f := s.Field(i)
    fmt.Printf("%d: %s %s = %v\n", i,
        typeOfT.Field(i).Name, f.Type(), f.Interface())
}
s.Field(0).SetInt(77)
s.Field(1).SetString("Sunset Strip")
fmt.Println("t is now", t)
```
output:
```
0: A int = 23
1: B string = skidoo
t is now {77 Sunset Strip}
```
需要注意的是，这里A，B字段都是导出的，同样，也只有可导出的字段才是可设置的。

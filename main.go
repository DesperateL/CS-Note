package main

import (
	"fmt"
	"strings"
)

func main() {
	// label1:
	// 	for i := 0; i < 10; i++ {
	// 		for j := 0; j < 10; j++ {
	// 			fmt.Println(i, j, "--")
	// 			if i+j > 15 {
	// 				break label1
	// 			}
	// 		}
	// 	}
	// 	fmt.Println("break label1")
	// 	for i := 0; i < 10; i++ {
	// 		for j := 0; j < 10; j++ {
	// 			fmt.Println(i, j, "++")
	// 			if i+j > 15 {
	// 				goto label1
	// 			}
	// 		}
	// 	}
	// 	fmt.Println("break label1")
	// 	goto END
	// 	fmt.Println("break label2")
	// END:
	// 	fmt.Println("break label3")
	//x := 10
	// for i := 0; i < 10; i++ {
	// 	switch {
	// 	case x%2 == 0:
	// 		fmt.Println(1)
	// 		//fallthrough
	// 	case x > 2:
	// 		fmt.Println(2)
	// 		break
	// 		//fallthrough
	// 	case x < 100:
	// 		fmt.Println(3)
	// 	}
	// }
	// ch := make(chan int)
	// go func() {
	// 	ch <- 10
	// }()
	// for {
	// 	fmt.Println("111")
	// 	select {
	// 	case <-ch:
	// 		break
	// 	case <-time.After(1 * time.Second):
	// 		fmt.Println("222")
	// 	}
	// }
	//i := 0
	// Start:
	// 	fmt.Println(i)
	// 	if i > 2 {
	// 		goto End
	// 	} else {
	// 		i += 1
	// 		goto Start
	// 	}
	// End:
	s := "172.161.32.2\n\r"
	fmt.Print(s)
	s1 := strings.Replace(s, "\n", "", -1)
	s1 = strings.Replace(s1, "\r", "", -1)

	fmt.Print(s1)
}

package main

import "fmt"

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
FirstLoop:
	for i := 0; i < 10; i++ {
		fmt.Println("sadf")
		for i := 0; i < 10; i++ {

			for i := 0; i < 10; i++ {
				break FirstLoop
			}
		}
	}
	goto Block
	{
	Block:
		v := 0
		fmt.Println(v)
	}
}

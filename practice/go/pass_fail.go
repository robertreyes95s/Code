// pass faule reports wether a grade is passing or failing
package main

import (
	"fmt"
	"bufio"
	"os"
	"log"
)

func main() {
	fmt.Print("Enter a grade: ")
	reader := bufio.NewReader(os.Stdin)
	input, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(input)
}

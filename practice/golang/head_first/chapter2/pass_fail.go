// This is program to determine wether a student
// has passed or failed a test
// This is a practice program
// this gives examples of packages, if..else staments 
// code blocks, and conversion, review notion notes 

package main

import (
	"fmt"
	"os"
	"bufio"
	"log"
	"strconv"
	"strings"
)

func main() {

	fmt.Print("Enter a grade: ")
	reader := bufio.NewReader(os.Stdin)
	input, err := reader.ReadString('\n')

	if err != nil {
		log.Fatal(err)
	}

	input = strings.TrimSpace(input)
	grade, err := strconv.ParseFloat(input, 64)

	if err != nil {
		log.Fatal(err)
	}

	var status string
	if grade >= 60 { 
		status = "passing"
	} else {
		status = "failing"
	}

	fmt.Println("A grade of" ,grade, "is", status)

}

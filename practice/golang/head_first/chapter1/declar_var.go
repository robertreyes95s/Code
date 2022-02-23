package main

import "fmt"

func main() { 
    // declaring var
    var quantity int
    var length, width float64
    var word rune

    // assign values to the variabes
    quantity = 4
    length, width = 1.2, 2.4
    word = 't'
    
    // using the variables
    fmt.Println(quantity)
    fmt.Println(length, width)
    fmt.Println(word)

    // Declare and assign in  the same line is also possible 
    var word string = "places"
    var num int = 45
    var name float = 45.5

}

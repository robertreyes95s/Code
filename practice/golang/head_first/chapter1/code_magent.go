// This is practice from the book 
// go head first

package main 

import (
    "fmt"
)

func main () {

    var original_count int = 10 
    var eaten_count int = 4
    var total int = original_count - eaten_count

    fmt.Println("I starte with",  original_count)
    fmt.Println("Some jerk are", eaten_count)
    fmt.Println("There are", total)


}


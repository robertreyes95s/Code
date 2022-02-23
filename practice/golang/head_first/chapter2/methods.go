// this program shows examples for using methods
// also an example for using the package strings
// and  it's methods 'NewReplacer' and 'Replacer'

package main

import (
	"fmt"
	"strings"
)

func main() {
	broken := "G# R#cks!"
	replacer := strings.NewReplacer("#", "o") //replacees # with o in string used
	fixed := replacer.Replace(broken)
	fmt.Println(fixed)
}

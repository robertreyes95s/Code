package main 
import (
	"fmt"
	"math/rand"
	"bufio"
	"os"
	
)
func main() {
// random number generator
	min := 1	
	max := 100
	random_num := rand.Intn(max - min) + min
	random_num = random_num

	// User entry 
	fmt.Print("Guess what number I'm thinking of!")
	guess := bufio.NewReader(os.Stdin)
	fmt.Println(guess)
	
	
}
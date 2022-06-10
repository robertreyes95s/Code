package main 

import "fmt"

func find_max(max int, water_amount int)  int { 
	var max_water int
	max_water = max - water_amount
	return max_water
}

func main() {
	var free_space int 
	bucket := 23
	amount_water := 15
	free_space = find_max(bucket, amount_water)
	fmt.Println("You can add", free_space, "liters of water till you hit the max")
}
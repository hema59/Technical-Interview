package main

import "fmt"
import "math"

func solution( array []int, a int, b int, c int) (int){
	arrayLength, count := len(array),0

	for i:= range array {
		for j:=i+1 ; j<arrayLength; j++{
			if math.Abs(int(array[i])-int(array[j])) > a { break }
			for k:=j+1 ; k<arrayLength; k++{
				if (math.Abs(array[j]-array[k]) <= b) & (math.Abs(array[i]-array[k])<=c) {
					count++
				}
			}
		}
	}
	return count
}

func main(){
	var a int8 = 7
	var b int8 = 2
	var c int8 = 3
	array := [...]int{3,0,1,1,9,7}
	fmt.Println(solution(array,a,b,c))
}
package main 

import (
	"fmt"
	// "math"
)

type geometry interface{
	area() float64
	perimeter() float64
}

type rectangle struct{
	length, width float64
}

type square struct{
	length float64 
}

func (r rectangle) area() float64{
	return r.length * r.width
}

func (r rectangle) perimeter() float64{
	return 2 * r.width + 2 * r.length
}

func (sq square) area() float64{
	return sq.length * sq.length
}

func (sq square) perimeter() float64{
	return 4 * sq.length 
}

func measure(g geometry){
	fmt.Println(g.area())
	fmt.Println(g.perimeter()) 
}

func main(){
	r := rectangle{
		width : 5,
		length : 10,
	}
	sq := square{
		length : 5,
	}

	measure(r)
	measure(sq) 
}

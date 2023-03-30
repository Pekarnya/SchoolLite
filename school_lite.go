//Package to describe basic geometry objects such as points, constants, etc
//Developer Afonya: tckachencko.grigorij@yandex.ru
//Alghorythms:

package main

import (
	"C"
	"math"
)

//Calculate center of line with using coordinates
//export centerLine
func centerLine(coordinates [4]float64) [2]float64{
	x1 := coordinates[0];
	y1 := coordinates[1];
	x2 := coordinates[2];
	y2 := coordinates[3];
	ox_cener := (x1 + x2) * 0.5
	oy_cener := (y1 + y2) * 0.5
	coordinates_array := [2]float64{ox_cener, oy_cener}
	return coordinates_array
}

//calculates the 2d distance between the two coordinates
//export distance
func distance(coordinates [4]float64) float64{
	distance := lineLength(coordinates)
	return distance
}

//declaring a struct array coordinate

//Return the coordinates tuple from the dictionary of python

//Return length from the coordinates
//export lineLength
func lineLength(coordinates [4]float64)float64{
	x1 := coordinates[0];
	y1 := coordinates[1];
	x2 := coordinates[2];
	y2 := coordinates[3];
	length := (math.Pow((y2 - y1), 2)) + (math.Pow((x2 - x1), 2))
	length = math.Sqrt(length)
	return math.Abs(length);
}


//Return the length of the figure from the coordinates
//export perimetr
func perimetr(vertices [][]float64) float64 {
	n := len(vertices)
	perimetr := 0.0
	//var length_figure float64
	for i := 0; i < n; i++ {
		j := (i + 1) % n
		coordinates := append(vertices[i], vertices[j]...)
		length := lineLength([4]float64(coordinates))
		
		perimetr = length + perimetr
	}
	return perimetr
}

//Area of simple poligon with using Gauss algorithm only for simple poligon
//export simplePolygonArea
func simplePolygonArea(vertices [][]float64) float64 {
    n := len(vertices)
    area := 0.0
    for i := 0; i < n; i++ {
        j := (i + 1) % n
        area += vertices[i][0]*vertices[j][1] - vertices[j][0]*vertices[i][1]
    }
    return math.Abs(area) / 2.0
}

//Angle calculates the angle between two vectors
//export angleCalc
func angleCalc(coordinates []float64) float64 {
	c := make(chan float64)
	den := make(chan float64)
	go perpendicularityCondition(coordinates, c)
	go denominator(coordinates, den)
	numerator := <- c
	denominator := <- den
	cos_angle := numerator / denominator
	angle := math.Acos(cos_angle) * (180 / pi)
	return angle
}

//Perpendicularity condition function x1 * x2 + y1 * y2
func perpendicularityCondition(coordinates []float64, c chan float64) {
	x1 := coordinates[0];
	y1 := coordinates[1];
	x2 := coordinates[2];
	y2 := coordinates[3];
	numerator := x1 * x2 + y1 * y2
	c <- numerator
}

//Denominator x^2 + y^2 * x2^2 + y^2
func denominator(coordinates []float64, den chan float64) {
	x1 := coordinates[0];
	y1 := coordinates[1];
	x2 := coordinates[2];
	y2 := coordinates[3];
	denominator := (math.Pow(x1, 2) + math.Pow(y1, 2)) * (math.Pow(x2, 2) + math.Pow(y2, 2))
	denominator = math.Sqrt(denominator)
	den <- math.Abs(denominator);
}

//Basic const for Pi
const pi float64 = math.Pi


func main() {
}

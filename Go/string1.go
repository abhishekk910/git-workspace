package main

import (
	"fmt"
	"strings"
)

// Golang program to check a string contains a specified substring
// func main(){
// 	var string1 = "Hello World"
// 	var sub_string = "World"
// 	if strings.Contains(string1, sub_string) == true{
// 		fmt.Printf("String (%s) contains sub-string (%s)", string1, sub_string)
// 	}else {
// 			fmt.Printf("String (%s) does not contains substring (%s)", string1, sub_string)
// 		}
// }


// Golang program to convert specified string to uppercase
// func main() {
// 	var str string = "Hello World"
// 	var result string
// 	result = strings.ToUpper(str)
// 	fmt.Println("String in uppercase : ", result)
// }


// Golang program to convert specified string
// in lowercase.
// func main() {
// 	var str string = "Hello World"
// 	var result string
// 	result = strings.ToLower(str)
// 	fmt.Println("String in lowercase : ", result)
// }


// Golang program to get the index of a specified character in the string
// func main() {
// 	var str string = "Hello World"
// 	var index int = 0
// 	index = strings.Index(str, "W")
// 	fmt.Println("Index is: ", index)
// }


// Golang program to get the length of the specified string.
// func main() {
// 	var str string = "Hello World"
// 	var length int 
// 	length = len(str)
// 	fmt.Println("Length of string is: ", length)
// }


// func main() {
// 	var str string = "Golang Programming Hello World"
// 	var strArr []string = strings.Split(str, " ")
// 	fmt.Println("Splited string:")
// 	for i := 0; i < len(strArr); i++ {
// 		fmt.Println(strArr[i])
// 	}
// }


// Golang program to demonstrate the strings.Repeat() function
// func main() {
// 	var str string = "Golang "
// 	var result string
// 	result = strings.Repeat(str, 4)
// 	fmt.Println("String After repetition: ", result)
// }

// Golang program to demonstrate the strings.Replace() function
// func main() {
// 	var str string = "Golang golang"
// 	var result1 string
// 	var result2 string

// 	//Replace specified character at all occurrences
// 	result1 = strings.Replace(str, "l", "L", -1)
// 	fmt.Println("Result1: ", result1)

// 	//Replace first occurrence of specified character
// 	result2 = strings.Replace(str, "l", "L", 3)
// 	fmt.Println("Result2: ", result2)
// }


// Golang program to demonstrate the strings.Join() function
// func main() {
// 	str := []string{"Green", "Orange", "White"}
// 	var result string
// 	fmt.Println(str)
// 	result = strings.Join(str, ",")
// 	fmt.Println("Result: ", result)
// }

// Golang program to check the specified substring is the prefix of the given string
// func main() {
// 	var str string = "Hello World"
// 	var substr string = "H"
// 	var result bool = false
// 	result = strings.HasPrefix(str, substr)
// 	if result == true {
// 		fmt.Println("Yes")
// 	} else {
// 		fmt.Println("No")
// 	}
// }

// Golang program to check the specified substring is the suffix of the given string
// func main() {
// 	var str string = "Hello World"
// 	var substr string = "12"
// 	var result bool = false
// 	result = strings.HasSuffix(str, substr)
// 	if result == true {
// 		fmt.Println("Yes")
// 	} else {
// 		fmt.Println("No")
// 	}
// }

// Golang program to count the total occurrences of a specified character in the specified string
// func main() {
// 	var str string = "Hello World"
// 	var result int 
// 	result = strings.Count(str, "l")
// 	fmt.Println("Total occurrence of 'i' in string: ", result)
// }


// Golang program to get characters from a string using the index
// func main() {
// 	str := "Hello World"
// 	for i := 0; i < len(str); i++ {
// 		fmt.Printf("%c\n", str[i])
// 	}
// }

// Golang program to print ASCII value of characters of the string
// func main() {
// 	str := "Hello World"
// 	fmt.Println("Ascii value of string:")
// 	for i := 0; i < len(str); i++ {
// 		fmt.Printf("%c  %d\n", str[i], str[i])
// 	}
// }


//Golang program to trim space from both ends of string using TrimSpace() function
// func main() {
// 	str := " Hello World "
// 	fmt.Printf("#%s#", strings.TrimSpace(str))
// }

// Golang program to trim specified characters from a string using Trim() function
// func main() {
// 	str := "!!Hello World%%"
// 	fmt.Printf("%s", strings.Trim(str, "!%"))
// }

// Golang program to trim specified characters from the left side of string using TrimLeft() function
// func main() {
// 	str := "!%Hello World!%"
// 	fmt.Printf("%s", strings.TrimLeft(str, "!%"))
// }

// Golang program to trim specified characters from the left side of string using TrimRight() function
// func main() {
// 	str := "!%Hello World!%"
// 	fmt.Printf("%s", strings.TrimRight(str, "!%"))
// }

// Golang program to demonstrate the strings.Compare() function
// func main() {
// 	str1 := "Hello"
// 	str2 := "hello"
// 	fmt.Println(strings.Compare(str1, str2))
// 	fmt.Println(strings.Compare(str2, str1))
// 	fmt.Println(strings.Compare(str1, str1))
// }


// func main() {
// 	str1 := "Hello World"
// 	str2 := "hello world"
// 	str3 := "HELLO WORLD"
// 	fmt.Println(strings.EqualFold(str1, str1))
// 	fmt.Println(strings.EqualFold(str1, str2))
// 	fmt.Println(strings.EqualFold(str1, str3))
// }


// func main() {
// 	str1 := "ABC PQR LMN PQR"
// 	str2 := "XYZ LMN LMN PQR"
// 	fmt.Println(strings.ReplaceAll(str1, "PQR", "TUV"))
// 	fmt.Println(strings.ReplaceAll(str2, "XYZ", "ABC"))
// }


// func main(){
// 	var string1 = "Hello World"
// 	for i:= range string1{
// 		fmt.Printf("%c\n",string1[i]) 
// 	}
// }


















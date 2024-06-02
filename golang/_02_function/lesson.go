package main

import "fmt"

// main является главной функцией программы и точкой входа. 
// Она вызывает несколько других функций для демонстрации их работы.
func main() {
	Great()
	PersonGreat("Alex")
	SeveralName("Alex", "Andy")

	var sum int = Sum(33, 9)
	fmt.Println(sum)

	sum, multiply := SumAndMultiply(13, 3)
	fmt.Printf("Sum = %d\nMultiply = %d\n", sum, multiply)

	sum_new, mult_new := namedSumAndMultiply(15, 2)
	fmt.Printf("Sum = %d\nMult = %d\n", sum_new, mult_new)
}

// Great выводит в консоль строку "Hello World!".
func Great() {
	fmt.Println("Hello World!")
}

// PersonGreat принимает строку name и выводит приветствие, содержащее это имя.
func PersonGreat(name string) {
	fmt.Printf("Hi %s\n", name)
}

// SeveralName принимает два имени и выводит приветствие, содержащее оба имени.
func SeveralName(name_1, name_2 string) {
	fmt.Printf("Hi everyone, %s and %s\n", name_1, name_2)
}

// Sum принимает два целых числа и возвращает их сумму.
func Sum(first, second int) int {
	return first + second
}

/*
В Go используется оператор ":=" для объявления и инициализации переменной одновременно. 
Этот оператор создает новую переменную и присваивает ей значение. 

Оператор "=" используется для присваивания значения уже объявленной переменной.
*/

/*
В этой функции переменные sum и multiply объявляются и инициализируются 
с помощью :=. 
Это создает новые переменные sum и multiply и сразу присваивает им значения.
*/
// SumAndMultiply принимает два целых числа и возвращает их сумму и произведение.
func SumAndMultiply(first_val, second_val int) (int, int) {
	sum := first_val + second_val
	multiply := first_val * second_val

	return sum, multiply
}

// В этой функции sum и multiply объявляются как именованные возвращаемые значения
/*
namedSumAndMultiply принимает два целых числа -
возвращает их сумму либо произведение.
Результаты возвращаются -
с использованием типизированных, именованных возвращаемых значений.
*/
func namedSumAndMultiply(first_val, second_val int) (sum int64, multiply int8) {
	sum = int64(first_val + second_val)
	multiply = int8(first_val * second_val)

	return
}

package main

import (
	"fmt"
	"unsafe"
)

// name - глобальная переменная
var name = "Alexandr"

// FULLNAME - глобальная константа (не может быть изменена)
const FULLNAME = "Andy"

func main() {
	// Ручное присваивание типа при инициализации переменной
	var hello string = "Hello!"
	fmt.Println(hello)

	// Объявление переменной с последующей инициализацией
	var helloFull string
	helloFull = "Hello!!"
	fmt.Println(helloFull)

	// Автоматическая типизация переменной
	ourBool := true
	fmt.Println(ourBool)

	// Вывод глобальной переменной
	fmt.Println(name)

	// Использование нового имени и форматированной строки
	newName := "Alex"
	congratulation := fmt.Sprintf("Hello! %s", newName) // f-строка

	// В Go нельзя объявлять переменные, которые не используются.
	// Использование пустого идентификатора для предотвращения ошибки.
	_ = congratulation

	// Приведение типов
	var num int64 = 15
	var num_2 int = 15

	fmt.Println(num + int64(num_2))

	// Посмотреть - сколько места занимают переменные разных типов
	var num_3 int8 = 100
	fmt.Println(unsafe.Sizeof(num_3)) // 1

	var num_4 int16 = 10000
	fmt.Println(unsafe.Sizeof(num_4)) // 2

	var num_5 int32 = 1000000000
	fmt.Println(unsafe.Sizeof(num_5)) // 4

	var num_6 int64 = 1000000000000000000
	fmt.Println(unsafe.Sizeof(num_6)) // 8
}

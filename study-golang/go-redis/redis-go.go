package main

import (
	"fmt"

	"gopkg.in/redis.v3"
)

func main() {

	client := redis.NewClient(&redis.Options{
		Addr: "localhost:6379",
	})

	stringcmd := client.Get("atintest")
	result := stringcmd.String()
	fmt.Println(result)
}

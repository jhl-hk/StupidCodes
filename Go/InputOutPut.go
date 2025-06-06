package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	// Create a new reader to read from standard input
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Enter a string: ")

	// Read input until newline
	input, err := reader.ReadString('\n')
	if err != nil {
		fmt.Println("Error reading input:", err)
		return
	}

	// Remove the newline character from the end
	input = strings.TrimSpace(input)

	// Output the original string plus something additional
	fmt.Printf("You entered: '%s'\n", input)
	fmt.Printf("Modified output: %s - Hello from Go!\n", input)
	fmt.Printf("Uppercase version: %s\n", strings.ToUpper(input))
	fmt.Printf("Length: %d characters\n", len(input))
}

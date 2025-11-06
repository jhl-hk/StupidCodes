package hk.jhl.test;

import java.util.Scanner;

public class Test1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Please input a three digit integer: ");
        int number = sc.nextInt();

        int digit = number % 10,
            ten = number / 10 % 10,
            hundred = number / 100 % 10;
        // Print different digit
        System.out.println("Digit: " + digit);
        System.out.println("Ten: " + ten);
        System.out.println("Hundred: " + hundred);
    }
}

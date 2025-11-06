package hk.jhl.test;

import java.util.Scanner;

public class Test3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Please input a number");
        int num = sc.nextInt();
        System.out.println("Please input a number");
        int num2 = sc.nextInt();

        System.out.println(num == 6 | num2 == 6 | (num + num2) % 6 == 0);
    }
}

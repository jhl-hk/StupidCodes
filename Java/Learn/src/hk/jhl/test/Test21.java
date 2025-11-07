package hk.jhl.test;

import java.util.Scanner;

public class Test21 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Input a number");
        int n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            if (i*i == n) {
                System.out.println(i);
                break;
            } else if (i * i > n) {
                System.out.println(i - 1);
                break;
            }
        }
    }
}

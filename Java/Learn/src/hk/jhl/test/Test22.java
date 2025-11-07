package hk.jhl.test;

import java.util.Scanner;

public class Test22 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Input a integer");
        int n = sc.nextInt();

        boolean flag = true;

        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                flag = false;
                // System.out.println(false);
                break;
            }
        }

        System.out.println(flag);
    }
}

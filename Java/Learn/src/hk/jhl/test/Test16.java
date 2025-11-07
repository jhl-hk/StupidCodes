package hk.jhl.test;

import java.util.Scanner;

public class Test16 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Start point");
        int x = sc.nextInt();
        System.out.println("End point");
        int y = sc.nextInt();

        int count = 0;
        for (int i = x; i <= y; i++) {
            if (i % 3 == 0 && i % 5 == 0) count++;
        }
        System.out.println(count);
    }
}

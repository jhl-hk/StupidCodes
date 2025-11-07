package hk.jhl.test;

import java.util.Random;
import java.util.Scanner;

public class Test23 {
    public static void main(String[] args) {
        Random r =  new Random();
        int n = r.nextInt(100) + 1; // 1 ~ 100
        int count = 0;

        while (true) {
            Scanner sc = new Scanner(System.in);
            System.out.println("Input a integer");
            int m = sc.nextInt();

            count ++;
            if (count == 3) {
                System.out.println("Failed");
                break;
            }

            if (m > n) {
                System.out.println("Large");
            } else if (m < n) {
                System.out.println("Small");
            } else  {
                System.out.println("Correct");
                break;
            }
        }
    }
}

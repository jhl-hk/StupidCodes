package hk.jhl.test;

import java.util.Scanner;

public class Test10 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Input a number to indicate a day");
        int week = sc.nextInt();

        switch (week) {
            case 1, 2, 3, 4, 5 -> System.out.println("Weekdays");
            case 6, 7 -> System.out.println("Weekends");
            default -> System.out.println("No such day");
        }
    }
}

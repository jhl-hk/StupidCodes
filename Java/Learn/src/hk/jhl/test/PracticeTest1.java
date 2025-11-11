package hk.jhl.test;

import java.util.Scanner;

public class PracticeTest1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Please input original price");
        int price = sc.nextInt();
        System.out.println("Please input current month");
        int month = sc.nextInt();
        System.out.println("Please input your 0 Eco, 1 Biz");
        int seat = sc.nextInt();

        if (month >= 5 && month <= 10) {
            price = discount(price, 0.9, 0.85, seat);
        } else if ((month >= 1 && month <= 4) || (month >= 11 && month <= 12)) {
            price = discount(price, 0.7, 0.65, seat);
        } else {
            System.out.println("Invalid month");
        }

        System.out.println(price);
    }

    public static int discount(int price, double biz, double eco, int seat) {
        if (seat == 1) {
            // cmd + alt + m
            price = (int) (price * biz);
        } else if (seat == 0) {
            price = (int) (price * eco);
        } else {
            System.out.println("Invalid seat");
        }

        return price;
    }
}

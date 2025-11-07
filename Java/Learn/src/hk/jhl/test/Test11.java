package hk.jhl.test;

import java.util.Scanner;

public class Test11 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Input your choice");
        int choice = sc.nextInt();
        switch (choice) {
            case 1:
                System.out.println("Check");
                break;
            case 2:
                System.out.println("Reservation");
                break;
            case 3:
                System.out.println("Alter");
                break;
            default:
                System.out.println("Exit");
                break;
        }
    }
}

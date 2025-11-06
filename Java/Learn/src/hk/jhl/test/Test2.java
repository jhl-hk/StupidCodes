package hk.jhl.test;

import java.util.Scanner;

public class Test2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Input my fashion");
        int myFashion = sc.nextInt();
        System.out.println("Input opponent fashion");
        int opponentFashion = sc.nextInt();

        boolean result = myFashion >  opponentFashion;

        System.out.println(result);
    }
}

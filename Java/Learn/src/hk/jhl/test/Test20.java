package hk.jhl.test;

public class Test20 {
    public static void main(String[] args) {
        // if 7 or 7x or 7*
        // from 1 to 100
        for (int i = 1; i <= 100; i++) {
            if (i % 10 == 7 || i / 10 % 10 == 7 || i % 7 == 0){
                System.out.println("Pass");
                continue;
            }
            System.out.println(i);
        }
    }
}

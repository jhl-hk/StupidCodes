package hk.jhl.test;

public class PracticeTest2 {
    public static void main(String[] args) {
        int count = 0;

        // Range 101 - 200
        for (int i = 101; i <= 200 ; i++) {
            boolean flag = true;
            // Judge current number is a prime
            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                count++;
            }
        }
        System.out.println(count);
    }
}

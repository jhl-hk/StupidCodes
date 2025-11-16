package hk.jhl.test;

import java.util.Random;

public class PracticeTest3 {
    public static void main(String[] args) {
        // A~Z a~z
        char[] chs = new char[52];
        for (int i = 0; i < chs.length; i++) {
            if (i <= 25) {
                // ASCII Codes
                // a --- 97
                chs[i] = (char) (97 + i);
            } else  {
                // A --- 65
                chs[i] = (char) (39 + i);
            }
        }

        String result = "";
        Random r = new Random();
        for (int i = 0; i < 4; i++) {
            int randomIndex = r.nextInt(chs.length);
            result += chs[randomIndex];
        }
        int num = r.nextInt(10);
        result += num;
        System.out.println(result);
    }
}

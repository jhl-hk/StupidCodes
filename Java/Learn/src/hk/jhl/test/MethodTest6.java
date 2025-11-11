package hk.jhl.test;

import java.util.Arrays;

public class MethodTest6 {
    public static void main(String[] args) {
        int[] arr = {1,4,16,15,1345,9999,111};
        System.out.println(getMax(arr));
    }

    public static int getMax(int[] arr) {
        int max = arr[0];

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }

        return max;
    }
}

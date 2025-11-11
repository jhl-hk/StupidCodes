package hk.jhl.test;

import java.util.Arrays;

public class MethodTest7 {
    public static void main(String[] args) {
        int[] arr = {1,1222,12341,12342,2345,62345};

        System.out.println(contains(arr, 122));
    }

    public static boolean contains(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if  (arr[i] == target) {
                return true;
            }
        }
        return false;
    }
}

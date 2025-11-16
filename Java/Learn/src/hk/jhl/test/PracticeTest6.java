package hk.jhl.test;

public class PracticeTest6 {
    public static void main(String[] args) {
        int num = 1983;
        int tempNum = num;
        int count = 0;

        while (tempNum != 0) {
            tempNum /= 10;
            count++;
        }

        int[] arr = new int[count];
        while (num != 0) {
            int digit = num % 10;
            num /= 10;
            count--;
            arr[count] = digit;
        }

        // int[] arr = {1,9,8,3};
        for (int i = 0; i < arr.length; i++) {
            arr[i] += 5;
        }
        for (int i = 0; i < arr.length; i++) {
            arr[i] %= 10;
        }
        for (int i = 0, j = arr.length - 1; i < j; i++, j--) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }

        int result = 0;
        for (int i = 0; i < arr.length; i++) {
            result = result * 10 + arr[i];
        }
        System.out.println(result);
    }
}

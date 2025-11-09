package hk.jhl.test;

public class ArrayTest7 {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5};

        int temp = arr[0];
        arr[0] = arr[4];
        arr[4] = temp;

        System.out.println(arr[0]);
        System.out.println(arr[4]);
    }
}

package hk.jhl.method;

public class MethodDemo5 {
    public static void main(String[] args) {
        int sum = getSum(10,20,30);
        System.out.println(sum);
    }

    public static int getSum(int a, int b, int c) {
        int  sum = a + b + c;
        return sum;
    }
}

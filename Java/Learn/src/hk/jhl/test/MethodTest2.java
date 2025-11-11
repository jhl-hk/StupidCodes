package hk.jhl.test;

public class MethodTest2 {
    public static void main(String[] args) {
        getCircleArea(12);
    }

    public static void getCircleArea(double radius) {
        double result = radius * 3.14;
        System.out.println(result);
    }
}

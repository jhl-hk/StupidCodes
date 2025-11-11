package hk.jhl.test;

public class MethodTest1 {
    public static void main(String[] args) {
        getLength(5.3, 1.3);
    }

    public static void getLength(double len, double width) {
        double result = (len + width) * 2;
        System.out.println(result);
    }
}

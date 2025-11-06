package hk.jhl.logicaloperator;

public class LogicaloperatorDemo1 {
    public static void main(String[] args) {
        // And
        System.out.println(true & true);
        System.out.println(false & true);
        System.out.println(true & false);
        System.out.println(false & false);

        // Or
        System.out.println(true | true);
        System.out.println(false | true);
        System.out.println(true | false);
        System.out.println(false | false);

        //
        System.out.println(true ^ true);
        System.out.println(false ^ true);
        System.out.println(true ^ false);
        System.out.println(false ^ false);

        System.out.println(!true);
        System.out.println(!false);

        // Shorten, if one is already true or false it will decide otherwise it will determine full
        // &&
        System.out.println(true && true);
        System.out.println(false && true);
        System.out.println(true && false);
        System.out.println(false && false);

        // ||
        System.out.println(true || true);
        System.out.println(false || true);
        System.out.println(true || false);
        System.out.println(false || false);

        int a = 20;
        int b = 30;
        System.out.println(a > b ? a : b);
    }
}

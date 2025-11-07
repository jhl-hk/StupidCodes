package hk.jhl.test;

public class Test17 {
    public static void main(String[] args) {
        int fold = 0, thickness = 1;
        while (thickness <= 88444300) {
            fold++;
            thickness *= 2;
        }
        System.out.println(fold);
    }
}

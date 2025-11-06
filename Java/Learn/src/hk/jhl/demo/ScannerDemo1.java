// import Scanner Package
import java.util.Scanner;

public class ScannerDemo1 {

  public static void main(String[] args) {
    // Create a Scanner object to read input from the console
    Scanner sc = new Scanner(System.in);

    System.out.println("Please entre an integer");
    // Recieve Data
    int i = sc.nextInt();
    System.out.println(i);
  }
}

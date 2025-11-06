public class VariableTest {

  public static void main(String[] args) {
    // Initially no person on the bus
    int people = 0;
    // 1st: person gets on the bus
    people++; // people = people + 1;
    // 2nd: two person gets on the bus, one person gets off the bus
    people += 2;
    people--; // people = people + 2 - 1;
    // 3rd: two person gets on the bus, one person gets off the bus
    people += 2;
    people--; // people = people + 2 - 1;
    // 4th: one person leaves the bus
    people--;
    // 5th: one person gets on the bus
    people++;

    // Print the result
    System.out.println(people);
  }
}

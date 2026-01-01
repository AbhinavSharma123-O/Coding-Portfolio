// FindMissing.java
public class FindMissing {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);

        // Sum of 1 to n
        int expectedSum = n * (n + 1) / 2;

        // Read n - 1 integers
        int actualSum = 0;
        while (!StdIn.isEmpty()) {
            actualSum += StdIn.readInt();
        }

        // Missing number
        int missing = expectedSum - actualSum;

        StdOut.println("Missing number: " + missing);
    }
}

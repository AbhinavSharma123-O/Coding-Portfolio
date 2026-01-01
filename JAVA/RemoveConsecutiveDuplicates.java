// RemoveConsecutiveDuplicates.java
public class RemoveConsecutiveDuplicates {
    public static void main(String[] args) {
        // If no input, do nothing
        if (StdIn.isEmpty()) {
            return;
        }

        // Read first token (assume integers)
        int prev = StdIn.readInt();
        StdOut.print(prev);

        // Read remaining tokens
        while (!StdIn.isEmpty()) {
            int x = StdIn.readInt();
            if (x != prev) {
                StdOut.print(" " + x);
                prev = x;
            }
        }
        StdOut.println();
    }
}

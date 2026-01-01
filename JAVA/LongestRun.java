// LongestRun.java
public class LongestRun {
    public static void main(String[] args) {
        if (StdIn.isEmpty()) {
            StdOut.println("No input");
            return;
        }
        int prev = StdIn.readInt();
        int bestValue = prev;
        int bestLen = 1;
        int currentLen = 1;
        while (!StdIn.isEmpty()) {
            int x = StdIn.readInt();
            if (x == prev) {
                currentLen++;
            } else {
                if (currentLen > bestLen) {
                    bestLen = currentLen;
                    bestValue = prev;
                }
                currentLen = 1;
                prev = x;
            }
        }
        // final check
        if (currentLen > bestLen) {
            bestLen = currentLen;
            bestValue = prev;
        }

        StdOut.println("Longest run: " + bestLen + " consecutive " + bestValue + (bestLen > 1 ? "s" : ""));
    }
}

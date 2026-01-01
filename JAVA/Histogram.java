// Histogram.java
public class Histogram {
    public static void main(String[] args) {
        if (args.length < 3) {
            StdOut.println("Usage: java Histogram <n> <lo> <hi>");
            return;
        }

        int n = Integer.parseInt(args[0]);
        double lo = Double.parseDouble(args[1]);
        double hi = Double.parseDouble(args[2]);

        if (n <= 0 || lo >= hi) {
            StdOut.println("Invalid arguments: require n>0 and lo<hi");
            return;
        }

        // counts for bins 0..n-1
        int[] counts = new int[n];

        // Read input values and increment the proper bin
        while (!StdIn.isEmpty()) {
            double x = StdIn.readDouble();
            if (x < lo || x > hi) continue;
            int bin = (int) ((x - lo) / (hi - lo) * n);
            if (bin < 0) bin = 0;
            if (bin >= n) bin = n - 1; // include x == hi into last bin
            counts[bin]++;
        }

        // Find max count for scaling
        int max = 0;
        for (int c : counts) if (c > max) max = c;
        if (max == 0) max = 1;

        // Set drawing scale: x from 0..n, y from 0..max*1.1 (small padding)
        StdDraw.setXscale(0, n);
        StdDraw.setYscale(0, max * 1.1);

        // Draw bars as filled rectangles centered at i+0.5 with half-width 0.4
        StdDraw.setPenRadius(0);
        for (int i = 0; i < n; i++) {
            double xcenter = i + 0.5;
            double halfWidth = 0.4;
            double height = counts[i];
            StdDraw.filledRectangle(xcenter, height / 2.0, halfWidth, height / 2.0);
        }

        // Optional: draw simple axes and labels
        StdDraw.setPenRadius(0.005);
        StdDraw.setPenColor(StdDraw.BLACK);
        // x ticks (bin indices)
        for (int i = 0; i <= n; i += Math.max(1, n/10)) {
            StdDraw.line(i, 0, i, -max*0.02);
        }
        StdOut.println("Histogram plotted (bins = " + n + ", lo = " + lo + ", hi = " + hi + ").");
    }
}

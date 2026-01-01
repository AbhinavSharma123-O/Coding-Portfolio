public class ShannonEntropy {
    public static void main(String[] args) {
        int m = Integer.parseInt(args[0]);
        int[] freq = new int[m + 1];

        int total = 0;
        while (!StdIn.isEmpty()) {
            int value = StdIn.readInt();
            if (value >= 1 && value <= m) {
                freq[value]++;
                total++;
            }
        }

        double entropy = 0.0;
        for (int i = 1; i <= m; i++) {
            if (freq[i] > 0) {
                double p = (double) freq[i] / total;
                entropy += -p * (Math.log(p) / Math.log(2));
            }
        }

        StdOut.printf("%.4f\n", entropy);
    }
}

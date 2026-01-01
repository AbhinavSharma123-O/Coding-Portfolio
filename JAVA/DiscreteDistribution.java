public class DiscreteDistribution {
    public static void main(String[] args) {
        int m = Integer.parseInt(args[0]);
        int n = args.length - 1;

        // read a[i]
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(args[i + 1]);
        }

        // compute cumulative sums
        int[] cum = new int[n + 1];
        cum[0] = 0;
        for (int i = 1; i <= n; i++) {
            cum[i] = cum[i - 1] + a[i - 1];
        }

        // sample m times
        for (int t = 0; t < m; t++) {
            int r = (int) (Math.random() * cum[n]);
            int i = 1;
            while (!(cum[i - 1] <= r && r < cum[i])) {
                i++;
            }
            System.out.print(i);
            if (t < m - 1) System.out.print(" ");
        }
        System.out.println();
    }
}

public class Birthday {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int trials = Integer.parseInt(args[1]);

        int[] counts = new int[n + 1];

        for (int t = 0; t < trials; t++) {
            boolean[] seen = new boolean[n];
            int people = 0;

            while (true) {
                int b = (int) (Math.random() * n);
                people++;
                if (seen[b]) break;
                seen[b] = true;
            }

            counts[people]++;
        }

        double cumulative = 0.0;

        for (int i = 1; i <= n; i++) {
            cumulative += (double) counts[i] / trials;
            System.out.println(i + "\t" + counts[i] + "\t" + cumulative);
            if (cumulative >= 0.5) break;
        }
    }
}

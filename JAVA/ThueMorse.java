public class ThueMorse {
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);

        // generate first n bits of Thue–Morse sequence
        int[] t = new int[n];
        t[0] = 0;

        for (int i = 1; i < n; i++) {
            int k = i & (i - 1);
            if (k == 0) t[i] = 1 - t[i - 1];
            else t[i] = t[k];
        }

        // print n×n weave pattern
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (t[i] == t[j]) System.out.print("+");
                else System.out.print("-");
                if (j < n - 1) System.out.print("  ");
            }
            System.out.println();
        }
    }
}

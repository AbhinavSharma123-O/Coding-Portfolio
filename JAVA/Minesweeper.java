public class Minesweeper {
    public static void main(String[] args) {
        int m = Integer.parseInt(args[0]);
        int n = Integer.parseInt(args[1]);
        int k = Integer.parseInt(args[2]);

        int total = m * n;

        // create array of all positions 0..mn-1
        int[] pos = new int[total];
        for (int i = 0; i < total; i++) pos[i] = i;

        // Fisher–Yates shuffle first k positions
        for (int i = 0; i < k; i++) {
            int r = i + (int) (Math.random() * (total - i));
            int tmp = pos[i];
            pos[i] = pos[r];
            pos[r] = tmp;
        }

        // mark mines
        boolean[][] mine = new boolean[m][n];
        for (int i = 0; i < k; i++) {
            int p = pos[i];
            mine[p / n][p % n] = true;
        }

        // compute and print
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (mine[r][c]) System.out.print("*");
                else {
                    int count = 0;
                    for (int rr = r - 1; rr <= r + 1; rr++) {
                        for (int cc = c - 1; cc <= c + 1; cc++) {
                            if (rr >= 0 && rr < m && cc >= 0 && cc < n) {
                                if (mine[rr][cc]) count++;
                            }
                        }
                    }
                    System.out.print(count);
                }
                if (c < n - 1) System.out.print("  ");
            }
            System.out.println();
        }
    }
}

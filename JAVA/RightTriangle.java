public class RightTriangle {
    public static void main(String[] args) {
        // parse three integer command-line arguments
        int x = Integer.parseInt(args[0]);
        int y = Integer.parseInt(args[1]);
        int z = Integer.parseInt(args[2]);

        // sort so a <= b <= c (all integers)
        int a = Math.min(x, Math.min(y, z));
        int c = Math.max(x, Math.max(y, z));
        int b = x + y + z - a - c;

        // compute squares with long to avoid overflow
        long aa = (long) a * a;
        long bb = (long) b * b;
        long cc = (long) c * c;

        // validity: all sides must be > 0 AND Pythagorean relation holds
        boolean positiveSides = (x > 0) && (y > 0) && (z > 0);
        boolean isPythagorean = (aa + bb) == cc;

        System.out.println(positiveSides && isPythagorean);
    }
}

// Spirograph.java
public class Spirograph {
    public static void main(String[] args) {
        double R = Double.parseDouble(args[0]);
        double r = Double.parseDouble(args[1]);
        double a = Double.parseDouble(args[2]);

        StdDraw.setXscale(-100, 100);
        StdDraw.setYscale(-100, 100);

        StdDraw.clear();
        StdDraw.setPenRadius(0.002);

        for (double t = 0.0; t < 10000; t += 0.01) {
            double x = (R + r) * Math.cos(t) - (r + a) * Math.cos(((R + r) / r) * t);
            double y = (R + r) * Math.sin(t) - (r + a) * Math.sin(((R + r) / r) * t);

            StdDraw.point(x, y);
        }

        StdOut.println("Spirograph drawn with R=" + R + ", r=" + r + ", a=" + a);
    }
}

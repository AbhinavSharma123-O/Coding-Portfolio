// AnimatedHeart.java
// Animated colored heart using StdDraw.
// Usage: java AnimatedHeart [steps] [delayMillis]
// Example: java AnimatedHeart 8000 0
public class AnimatedHeart {
    public static void main(String[] args) {
        int steps = args.length >= 1 ? Integer.parseInt(args[0]) : 10000;
        int delay = args.length >= 2 ? Integer.parseInt(args[1]) : 0; // ms

        // Parametric heart (classic)
        // x(t) = 16 sin^3 t
        // y(t) = 13 cos t - 5 cos(2t) - 2 cos(3t) - cos(4t)
        // We'll scale it to fit nicely on the canvas.

        // Determine scale to use
        double scale = 12.0; // roughly fits the -16..16 x-range into canvas

        StdDraw.enableDoubleBuffering();
        StdDraw.clear();
        StdDraw.setPenRadius(0.002);

        // set coordinate system a little larger than curve extents
        StdDraw.setXscale(-scale, scale);
        StdDraw.setYscale(-scale, scale);

        // Starting point at t = 0
        double prevX = heartX(0) * 1.0;
        double prevY = heartY(0) * 1.0;

        // Draw in many small segments; step t from 0 .. 2*pi (we can repeat to thicken)
        double twoPi = 2 * Math.PI;

        for (int i = 1; i <= steps; i++) {
            double t = (double)i / steps * twoPi;

            double x = heartX(t);
            double y = heartY(t);

            // color: vary from deep red to pink using hue near red
            // We'll convert a hue-based color to an approximate red-pink gradient.
            // Use HSB: hue ~ 0 (red), vary brightness/saturation to get pinkish.
            float fraction = (float)i / steps;
            float hue = 0.0f; // red
            float saturation = 0.6f + 0.4f * (float)Math.sin(fraction * Math.PI);
            float brightness = 0.7f + 0.3f * (float)Math.cos(fraction * Math.PI);
            java.awt.Color color = java.awt.Color.getHSBColor(hue, saturation, brightness);
            StdDraw.setPenColor(color);

            // Draw a short line segment from previous point to this point (makes a continuous curve)
            StdDraw.line(prevX, prevY, x, y);

            prevX = x;
            prevY = y;

            // occasionally flush (and pause slightly for animation)
            if (i % 200 == 0) {
                StdDraw.show(delay);
            }
        }

        // final flush
        StdDraw.show(0);

        StdOut.println("Animated heart drawn (" + steps + " steps).");
    }

    // heart param functions (unscaled)
    private static double heartX(double t) {
        double s = Math.sin(t);
        return 16 * s * s * s / 1.0; // /1.0 kept to show it's the raw formula
    }

    private static double heartY(double t) {
        double c = Math.cos(t);
        return (13 * c - 5 * Math.cos(2*t) - 2 * Math.cos(3*t) - Math.cos(4*t)) / 1.0;
    }
}

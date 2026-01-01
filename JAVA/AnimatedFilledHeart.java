// AnimatedFilledHeart.java
// Draws a filled heart on a black background, animates its formation, then pulses.
// Usage: java AnimatedFilledHeart [steps] [formFrames] [pulseHz]
// Examples:
//   java AnimatedFilledHeart
//   java AnimatedFilledHeart 1200 200 1.0

import java.awt.Color;

public class AnimatedFilledHeart {

    public static void main(String[] args) {
        // number of sample points used to construct the heart (higher -> smoother)
        int steps = args.length >= 1 ? Integer.parseInt(args[0]) : 1200;
        // how many animation frames to fully form the heart
        int formFrames = args.length >= 2 ? Integer.parseInt(args[1]) : 200;
        // pulse frequency in Hz (beats per second)
        double pulseHz = args.length >= 3 ? Double.parseDouble(args[2]) : 1.0;

        // coordinate scaling chosen to fit the classic heart nicely
        double scale = 12.0;

        // Prepare points for t in [0, 2*pi]
        double[] baseX = new double[steps + 1];
        double[] baseY = new double[steps + 1];
        for (int i = 0; i <= steps; i++) {
            double t = (double)i / steps * 2.0 * Math.PI;
            baseX[i] = heartX(t);
            baseY[i] = heartY(t);
        }

        // Setup StdDraw
        StdDraw.enableDoubleBuffering();
        StdDraw.setXscale(-scale, scale);
        StdDraw.setYscale(-scale, scale);
        StdDraw.setPenRadius(0.002);

        // Black background
        Color bg = Color.BLACK;

        // Animation: first "forming" stage, then continuous pulsing
        // Form: progressively draw more of the polygon until full
        for (int frame = 1; frame <= formFrames; frame++) {
            double fraction = (double) frame / formFrames; // 0..1
            int pointsToDraw = Math.max(4, (int) (fraction * steps));

            StdDraw.clear(bg);

            // build scaled polygon for current fraction and a neutral scale (no pulse yet)
            double[] xs = new double[pointsToDraw + 1];
            double[] ys = new double[pointsToDraw + 1];
            for (int i = 0; i < pointsToDraw; i++) {
                xs[i] = baseX[i] * 0.9; // small base scale to fit nicely
                ys[i] = baseY[i] * 0.9;
            }
            // close polygon to ensure fill
            xs[pointsToDraw] = xs[0];
            ys[pointsToDraw] = ys[0];

            // Fill color that looks warm (pink-red)
            Color fill = new Color(220, 16, 64); // deep red
            StdDraw.setPenColor(fill);
            StdDraw.filledPolygon(xs, ys);

            // outline slightly brighter
            StdDraw.setPenColor(new Color(255, 80, 100));
            StdDraw.polygon(xs, ys);

            StdDraw.show(20); // small delay so formation is visible
        }

        // Now the heart is complete — enter pulse loop
        long t0 = System.currentTimeMillis();
        double pulseAmp = 0.06;   // amplitude of scale variation (6%)
        double baseScale = 0.95;  // base overall scale
        int flushEvery = 2;       // flush occasionally for smooth animation
        int iFrame = 0;

        while (true) {
            iFrame++;
            double elapsed = (System.currentTimeMillis() - t0) / 1000.0; // seconds
            // sinusoidal pulse, range [-1, 1]
            double pulse = Math.sin(2.0 * Math.PI * pulseHz * elapsed);
            double currentScale = baseScale * (1.0 + pulseAmp * pulse);

            StdDraw.clear(bg);

            // create scaled polygon of whole heart
            double[] xs = new double[steps + 1];
            double[] ys = new double[steps + 1];
            for (int i = 0; i <= steps; i++) {
                xs[i] = baseX[i] * currentScale;
                ys[i] = baseY[i] * currentScale;
            }

            // To get a nice filled look with slight radial brightness, draw multiple
            // filled polygons with slightly different sizes and alpha blends.
            // StdDraw doesn't support alpha easily, so we emulate by layering colors.
            // Outer soft layer
            StdDraw.setPenColor(new Color(120, 10, 30)); // deep darker
            double[] xsOuter = scaleArray(xs, 1.06);
            double[] ysOuter = scaleArray(ys, 1.06);
            StdDraw.filledPolygon(xsOuter, ysOuter);

            // main fill
            StdDraw.setPenColor(new Color(220, 20, 80)); // main red-pink
            StdDraw.filledPolygon(xs, ys);

            // bright inner highlight (slightly smaller)
            StdDraw.setPenColor(new Color(255, 140, 160));
            double[] xsInner = scaleArray(xs, 0.96);
            double[] ysInner = scaleArray(ys, 0.96);
            StdDraw.filledPolygon(xsInner, ysInner);

            // outline
            StdDraw.setPenColor(new Color(255, 100, 120));
            StdDraw.polygon(xs, ys);

            // optional little shine: a small white-ish overlay near top-left of heart
            double shineX = -3.5 * currentScale;
            double shineY = 7.5 * currentScale;
            StdDraw.setPenColor(new Color(255, 220, 230));
            StdDraw.filledCircle(shineX, shineY, 0.5 * currentScale);

            // paint to screen
            if (iFrame % flushEvery == 0) StdDraw.show(10);
            else StdDraw.show(0);

            // allow escape: if user closes window or presses ctrl-c, program will stop externally.
            // (StdDraw doesn't provide a direct "window closed" query in the Princeton lib).
        }
    }

    // Classic heart param (unscaled)
    private static double heartX(double t) {
        double s = Math.sin(t);
        return 16 * s * s * s / 18.0 * 12.0 / 12.0; // keep raw proportion; scaling is applied later
    }

    private static double heartY(double t) {
        double c = Math.cos(t);
        return (13 * c - 5 * Math.cos(2*t) - 2 * Math.cos(3*t) - Math.cos(4*t)) / 18.0 * 12.0 / 12.0;
    }

    private static double[] scaleArray(double[] arr, double factor) {
        double[] out = new double[arr.length];
        for (int i = 0; i < arr.length; i++) out[i] = arr[i] * factor;
        return out;
    }
}

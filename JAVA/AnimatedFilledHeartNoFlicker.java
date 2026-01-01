// AnimatedFilledHeartNoFlicker.java
// Draws a larger filled heart on a black background with a smooth, non-flickering forming animation.
// Usage: javac AnimatedFilledHeartNoFlicker.java
//        java AnimatedFilledHeartNoFlicker [steps] [formFrames]

import java.awt.Color;
import java.awt.Font;

public class AnimatedFilledHeartNoFlicker {

    public static void main(String[] args) {
        int steps = args.length >= 1 ? Integer.parseInt(args[0]) : 1600;   // resolution
        int formFrames = args.length >= 2 ? Integer.parseInt(args[1]) : 240; // formation frames

        double canvasScale = 14.0;         // world coordinate range +/- canvasScale
        double rawScaleFactor = 0.55;      // scale applied to raw parametric heart

        // Precompute parametric heart points
        double[] baseX = new double[steps + 1];
        double[] baseY = new double[steps + 1];
        for (int i = 0; i <= steps; i++) {
            double t = (double) i / steps * 2.0 * Math.PI;
            baseX[i] = 16 * Math.pow(Math.sin(t), 3);
            baseY[i] = 13 * Math.cos(t) - 5 * Math.cos(2 * t) - 2 * Math.cos(3 * t) - Math.cos(4 * t);
        }

        // StdDraw setup
        StdDraw.enableDoubleBuffering();
        StdDraw.setXscale(-canvasScale, canvasScale);
        StdDraw.setYscale(-canvasScale, canvasScale);
        StdDraw.setPenRadius(0.002);

        Color bg = Color.BLACK;
        Color outer = new Color(90, 10, 30);
        Color mainFill = new Color(220, 20, 80);
        Color highlight = new Color(255, 140, 160);
        Color outline = new Color(255, 100, 120);

        // Reusable arrays for polygon frames (avoid allocating inside loop)
        double[] xs = new double[steps + 1];
        double[] ys = new double[steps + 1];

        // FORMING: draw more points each frame; draw full frame offscreen then show once
        for (int frame = 1; frame <= formFrames; frame++) {
            double fraction = (double) frame / Math.max(1, formFrames);
            int points = Math.max(6, (int) (fraction * steps));

            // Build final polygon arrays for this frame (closed polygon)
            for (int i = 0; i < points; i++) {
                xs[i] = baseX[i] * rawScaleFactor * 1.05; // slightly larger base
                ys[i] = baseY[i] * rawScaleFactor * 1.05;
            }
            xs[points] = xs[0];
            ys[points] = ys[0];

            // Draw everything into back buffer BEFORE showing
            StdDraw.clear(bg);

            // layered fills (drawn in offscreen buffer)
            StdDraw.setPenColor(outer);
            StdDraw.filledPolygon(scaleArray(xs, points + 1, 1.06), scaleArray(ys, points + 1, 1.06));

            StdDraw.setPenColor(mainFill);
            StdDraw.filledPolygon(xs, ys);

            StdDraw.setPenColor(highlight);
            StdDraw.filledPolygon(scaleArray(xs, points + 1, 0.96), scaleArray(ys, points + 1, 0.96));

            StdDraw.setPenColor(outline);
            StdDraw.polygon(xs, ys);

            // Single show call per frame (no other show/clear inside frame)
            StdDraw.show(18); // ~18 ms pause gives smooth forming; increase to slow it
        }

        // FINAL static heart
        // Build full polygon arrays
        for (int i = 0; i <= steps; i++) {
            xs[i] = baseX[i] * rawScaleFactor * 1.10; // final heart slightly bigger
            ys[i] = baseY[i] * rawScaleFactor * 1.10;
        }

        StdDraw.clear(bg);

        // Draw layers once, then show once
        StdDraw.setPenColor(outer);
        StdDraw.filledPolygon(scaleArray(xs, steps + 1, 1.06), scaleArray(ys, steps + 1, 1.06));

        StdDraw.setPenColor(mainFill);
        StdDraw.filledPolygon(xs, ys);

        StdDraw.setPenColor(highlight);
        StdDraw.filledPolygon(scaleArray(xs, steps + 1, 0.96), scaleArray(ys, steps + 1, 0.96));

        StdDraw.setPenColor(outline);
        StdDraw.polygon(xs, ys);

        // Text "From Abhinav" centered below
        StdDraw.setPenColor(Color.WHITE);
        StdDraw.setFont(new Font("SansSerif", Font.BOLD, 28));
        StdDraw.text(0, -9.8, "From Abhinav");

        StdDraw.show(0); // final show, no flicker
        StdOut.println("Done.");
    }

    // scale portion of array (only first n elements) into new array for StdDraw methods
    private static double[] scaleArray(double[] arr, int n, double factor) {
        double[] out = new double[n];
        for (int i = 0; i < n; i++) out[i] = arr[i] * factor;
        return out;
    }
}

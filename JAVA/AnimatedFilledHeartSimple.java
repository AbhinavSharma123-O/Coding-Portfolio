
// Draws a larger filled heart on a black background, animates its formation,
// then displays "From Abhinav" centered below the heart.
//
// Usage: java AnimatedFilledHeartSimple [steps] [formFrames]
// Example: java AnimatedFilledHeartSimple 1600 240

import java.awt.Color;
import java.awt.Font;

public class AnimatedFilledHeartSimple {

    public static void main(String[] args) {
        int steps = args.length >= 1 ? Integer.parseInt(args[0]) : 1600;   // smoother by default
        int formFrames = args.length >= 2 ? Integer.parseInt(args[1]) : 240;

        // overall coordinate scaling � larger heart fits nicely
        double scale = 14.0;

        // Precompute parametric heart points for t in [0, 2*pi]
        double[] baseX = new double[steps + 1];
        double[] baseY = new double[steps + 1];
        for (int i = 0; i <= steps; i++) {
            double t = (double)i / steps * 2.0 * Math.PI;
            // classic parametric heart
            baseX[i] = 16 * Math.pow(Math.sin(t), 3);
            baseY[i] = 13 * Math.cos(t) - 5 * Math.cos(2*t) - 2 * Math.cos(3*t) - Math.cos(4*t);
        }

        StdDraw.enableDoubleBuffering();
        StdDraw.setXscale(-scale, scale);
        StdDraw.setYscale(-scale, scale);
        StdDraw.setPenRadius(0.002);

        Color bg = Color.BLACK;
        // Colors for layers
        Color outer = new Color(90, 10, 30);       // dark halo
        Color mainFill = new Color(220, 20, 80);   // main red
        Color highlight = new Color(255, 140, 160);// inner highlight
        Color outline = new Color(255, 100, 120);

        // FORMING ANIMATION: progressively draw more of the polygon until full
        for (int frame = 1; frame <= formFrames; frame++) {
            double fraction = (double) frame / formFrames; // 0..1
            int pointsToDraw = Math.max(6, (int)(fraction * steps));

            StdDraw.clear(bg);

            // build polygon arrays sized to current portion
            double[] xs = new double[pointsToDraw + 1];
            double[] ys = new double[pointsToDraw + 1];
            // slightly larger base scale to make the heart bigger
            double baseScale = 1.05;
            for (int i = 0; i < pointsToDraw; i++) {
                xs[i] = baseX[i] * (baseScale * 0.55); // scale down param raw numbers to fit the canvas
                ys[i] = baseY[i] * (baseScale * 0.55);
            }
            // close polygon
            xs[pointsToDraw] = xs[0];
            ys[pointsToDraw] = ys[0];

            // Draw layered fill for nicer look
            StdDraw.setPenColor(outer);
            StdDraw.filledPolygon(scaleArray(xs, 1.06), scaleArray(ys, 1.06));

            StdDraw.setPenColor(mainFill);
            StdDraw.filledPolygon(xs, ys);

            StdDraw.setPenColor(highlight);
            StdDraw.filledPolygon(scaleArray(xs, 0.96), scaleArray(ys, 0.96));

            StdDraw.setPenColor(outline);
            StdDraw.polygon(xs, ys);

            // show frame (small pause so formation is visible)
            StdDraw.show(16);
        }

        // FINAL STATIC HEART (bigger and centered)
        StdDraw.clear(bg);

        double finalScale = 1.1 * 0.55; // tweak to make final heart a bit bigger overall
        double[] xsFinal = new double[steps + 1];
        double[] ysFinal = new double[steps + 1];
        for (int i = 0; i <= steps; i++) {
            xsFinal[i] = baseX[i] * finalScale;
            ysFinal[i] = baseY[i] * finalScale;
        }

        // outer halo
        StdDraw.setPenColor(outer);
        StdDraw.filledPolygon(scaleArray(xsFinal, 1.06), scaleArray(ysFinal, 1.06));

        // main fill
        StdDraw.setPenColor(mainFill);
        StdDraw.filledPolygon(xsFinal, ysFinal);

        // inner highlight
        StdDraw.setPenColor(highlight);
        StdDraw.filledPolygon(scaleArray(xsFinal, 0.96), scaleArray(ysFinal, 0.96));

        // outline
        StdDraw.setPenColor(outline);
        StdDraw.polygon(xsFinal, ysFinal);

        // Write "From Abhinav" centered below the heart
        StdDraw.setPenColor(Color.WHITE);
        Font font = new Font("SansSerif", Font.BOLD, 28); // adjust size if desired
        StdDraw.setFont(font);
        // choose a y coordinate below the heart so it doesn't overlap
        double textY = -9.8; // tuned for scale = 14.0 and finalScale used above
        StdDraw.text(0, textY, "From Abhinav");

        StdDraw.show(0);

        StdOut.println("Done: filled heart drawn. Message: From Abhinav");
    }

    // helper to scale arrays (shallow copy)
    private static double[] scaleArray(double[] arr, double factor) {
        double[] out = new double[arr.length];
        for (int i = 0; i < arr.length; i++) out[i] = arr[i] * factor;
        return out;
    }
}

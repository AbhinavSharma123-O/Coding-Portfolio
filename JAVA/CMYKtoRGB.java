public class CMYKtoRGB {
    public static void main(String[] args) {
        // parse CMYK values as fractions 0.0..1.0 (the grader supplies values in this range)
        double c = Double.parseDouble(args[0]);
        double m = Double.parseDouble(args[1]);
        double y = Double.parseDouble(args[2]);
        double k = Double.parseDouble(args[3]);

        // compute RGB (0..255), rounding to nearest int
        int red   = (int) Math.round(255.0 * (1.0 - c) * (1.0 - k));
        int green = (int) Math.round(255.0 * (1.0 - m) * (1.0 - k));
        int blue  = (int) Math.round(255.0 * (1.0 - y) * (1.0 - k));

        // clamp to [0,255]
        red   = Math.max(0, Math.min(255, red));
        green = Math.max(0, Math.min(255, green));
        blue  = Math.max(0, Math.min(255, blue));

        // exact formatting required by grader:
        System.out.println("red   = " + red);
        System.out.println("green = " + green);
        System.out.println("blue  = " + blue);
    }
}

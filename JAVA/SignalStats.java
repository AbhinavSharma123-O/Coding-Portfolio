// SignalStats.java
public class SignalStats {
    public static void main(String[] args) {
        double sumMagnitude = 0.0;
        double sumPower = 0.0;
        int count = 0;
        int zeroCrossings = 0;

        // prevSign: 0 = unknown/no non-zero yet, +1 = positive, -1 = negative
        int prevSign = 0;

        while (!StdIn.isEmpty()) {
            double x = StdIn.readDouble();
            sumMagnitude += Math.abs(x);
            sumPower += x * x;
            count++;

            int sign = 0;
            if (x > 0) sign = 1;
            else if (x < 0) sign = -1;

            if (sign != 0) {
                if (prevSign != 0 && sign != prevSign) {
                    zeroCrossings++;
                }
                prevSign = sign;
            }
            // if sign==0, do not update prevSign (ignore zeros for sign changes)
        }

        if (count == 0) {
            StdOut.println("No input");
            return;
        }

        double avgMagnitude = sumMagnitude / count;
        double avgPower = sumPower / count;

        StdOut.println("Average magnitude = " + String.format("%.6f", avgMagnitude));
        StdOut.println("Average power     = " + String.format("%.6f", avgPower));
        StdOut.println("Zero crossings    = " + zeroCrossings);
    }
}

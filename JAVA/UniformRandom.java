public class UniformRandom {
    public static void main(String[] args) {

        double a = Math.random();
        double b = Math.random();
        double c = Math.random();
        double d = Math.random();
        double e = Math.random();

        // Compute sum
        double sum = a + b + c + d + e;

        // Compute average
        double avg = sum / 5.0;

        // Compute min (nested Math.min)
        double min = Math.min(a, Math.min(b, Math.min(c, Math.min(d, e))));

        // Compute max (nested Math.max)
        double max = Math.max(a, Math.max(b, Math.max(c, Math.max(d, e))));

        System.out.println("Values:");
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        System.out.println(d);
        System.out.println(e);

        System.out.println("\nAverage = " + avg);
        System.out.println("Min     = " + min);
        System.out.println("Max     = " + max);
    }
}

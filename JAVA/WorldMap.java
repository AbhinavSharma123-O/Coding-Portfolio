public class WorldMap {
    public static void main(String[] args) {
        int width = StdIn.readInt();
        int height = StdIn.readInt();

        StdDraw.setCanvasSize(width, height);
        StdDraw.setXscale(0, width);
        StdDraw.setYscale(0, height);

        while (!StdIn.isEmpty()) {
            String name = StdIn.readString();
            int vertices = StdIn.readInt();

            double[] xs = new double[vertices];
            double[] ys = new double[vertices];

            for (int i = 0; i < vertices; i++) {
                xs[i] = StdIn.readDouble();
                ys[i] = StdIn.readDouble();
            }

            StdDraw.polygon(xs, ys);
        }
    }
}

public class BandMatrix {
public static void main(String[] args) {
if (args.length < 2) {
System.out.println("Usage: java BandMatrix n width");
return;
}
int n = Integer.parseInt(args[0]);
int width = Integer.parseInt(args[1]);
for (int i = 0; i < n; i++) {
StringBuilder sb = new StringBuilder();
for (int j = 0; j < n; j++) {
int dist = Math.abs(i - j); // distance to main diagonal
if (dist <= width) sb.append("* ");
else sb.append("0 ");
}
System.out.println(sb.toString());
}
}
}
public class RandomWalker {
public static void main(String[] args) {
if (args.length < 1) {
System.out.println("Usage: java RandomWalker r");
return;
}
int r = Integer.parseInt(args[0]);
int x = 0;
int y = 0;
int steps = 0;
System.out.println("(0, 0)");
while (Math.abs(x) + Math.abs(y) < r) {
double p = Math.random();
if (p < 0.25) {
y++; // north
} else if (p < 0.5) {
x++; // east
} else if (p < 0.75) {
y--; // south
} else {
x--; // west
}
steps++;
System.out.println("(" + x + ", " + y + ")");
}
System.out.println("steps = " + steps);
}
}
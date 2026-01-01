public class RandomWalkers {
public static void main(String[] args) {
if (args.length < 2) {
System.out.println("Usage: java RandomWalkers r trials");
return;
}
int r = Integer.parseInt(args[0]);
int trials = Integer.parseInt(args[1]);
long totalSteps = 0L;
for (int t = 0; t < trials; t++) {
int x = 0, y = 0, steps = 0;
while (Math.abs(x) + Math.abs(y) < r) {
double p = Math.random();
if (p < 0.25) y++;
else if (p < 0.5) x++;
else if (p < 0.75) y--;
else x--;
steps++;
}
totalSteps += steps;
}
double average = totalSteps / (double) trials;
System.out.println("average number of steps = " + average);
}
}
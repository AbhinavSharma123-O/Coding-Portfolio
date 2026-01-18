import java.util.Scanner;
public class NumberCheck {
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
System.out.print("Enter number: ");
int n = sc.nextInt();
int temp = n, sum = 0;
while (temp > 0) {
sum += temp % 10;
temp /= 10;}
System.out.println("Sum is: " + sum);
boolean prime = sum > 1;
for (int i = 2; i<= sum / 2; i++) {
if (sum % i == 0) {
prime = false;
break;}}
temp = sum;
int arm = 0;
while (temp > 0) {
int d = temp % 10;
arm += d * d * d;
temp /= 10;}
int perfect = 0;
for (int i = 1; i< sum; i++) {
if (sum % i == 0)
perfect += i;}
System.out.println("Prime: " + (prime ? "Y" : "N"));
System.out.println("Armstrong: " + (arm == sum ? "Y" : "N"));
System.out.println("Perfect: " + (perfect == sum ? "Y" : "N"));}}

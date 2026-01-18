import java.util.Scanner;
public class ConvertNumber {
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
int n = sc.nextInt();
int temp = n;
String binary = "";
while (temp > 0) {
binary = (temp % 2) + binary;
temp /= 2;}
temp = n;
String hex = "";
char hexChar[] = "0123456789ABCDEF".toCharArray();
while (temp > 0) {
hex = hexChar[temp % 16] + hex;
temp /= 16;}
System.out.println("Binary: " + binary);
System.out.println("Hexadecimal: " + hex);}}

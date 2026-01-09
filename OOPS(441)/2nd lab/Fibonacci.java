import java.util.Scanner;
class Fibonacci{
    public static void main(String[]args){
	int num=0;
	Scanner sc=new Scanner(System.in);
        System.out.print("ENter the NUm");
        num=sc.nextInt();
	int i=0;
	int z=0;
	int p=0;
	int q=1;
	while (i<=num){
		System.out.println(p+q);
		z=p+q;
		p=q;
		q=z;
		i++;}}}
		
	
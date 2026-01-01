public class Random{
  public static void main(String[] args){
    int N = Integer.parseInt(args[0]);
    double r = Math.random();   // 0 ? r < 1
    int value = (int)(r * N);   // truncates ? 0 to N-1
    System.out.println(value);
  }}
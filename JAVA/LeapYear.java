public class LeapYear {
    public static void main(String[] args) {
        int year = Integer.parseInt(args[0]);

        boolean leap = (year % 400 == 0) ||
                       (year % 4 == 0 && year % 100 != 0);

        System.out.println(leap);
    }
}

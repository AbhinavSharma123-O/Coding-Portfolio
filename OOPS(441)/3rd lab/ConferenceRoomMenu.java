import java.util.Scanner;
class ConferenceRoomMenu {
    static String[][] bookings = new String[10][4];
    static int count = 0;
    static void bookRoom(String date, int start, int end, String name) {
        for (int i = 0; i < count; i++) {
            if (bookings[i][0].equals(date)) {
                int s = Integer.parseInt(bookings[i][1]);
                int e = Integer.parseInt(bookings[i][2]);
                if (start < e && end > s) {
                    System.out.println("Room already booked for this time.");
                    return;
                }}}
        bookings[count][0] = date;
        bookings[count][1] = String.valueOf(start);
        bookings[count][2] = String.valueOf(end);
        bookings[count][3] = name;
        count++;
        System.out.println("Room booked successfully.");
    }
    static void checkAvailability(String date, int start, int end) {
        for (int i = 0; i < count; i++) {
            if (bookings[i][0].equals(date)) {
                int s = Integer.parseInt(bookings[i][1]);
                int e = Integer.parseInt(bookings[i][2]);
                if (start < e && end > s) {
                    System.out.println(" Room is NOT available.");
                    return;}
            }
        }
        System.out.println("Room is available.");
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int choice;
        do {
            System.out.println("\nConference Room Menu");
            System.out.println("1. Book Room");
            System.out.println("2. Check Availability");
            System.out.println("3. Exit");
            System.out.print("Enter choice: ");
            choice = sc.nextInt();
            sc.nextLine();
            switch (choice) {
                case 1:
                    System.out.print("Enter Date (dd-mm-yyyy): ");
                    String date = sc.nextLine();
                    System.out.print("Enter Start Time (hour): ");
                    int start = sc.nextInt();
                    System.out.print("Enter End Time (hour): ");
                    int end = sc.nextInt();
                    sc.nextLine();
                    System.out.print("Enter Your Name: ");
                    String name = sc.nextLine();
                    bookRoom(date, start, end, name);
                    break;
                case 2:
                    System.out.print("Enter Date (dd-mm-yyyy): ");
                    String d = sc.nextLine();
                    System.out.print("Enter Start Time (hour): ");
                    int s = sc.nextInt();
                    System.out.print("Enter End Time (hour): ");
                    int e = sc.nextInt();
                    checkAvailability(d, s, e);
                    break;
                case 3:
                    System.out.println("Exiting program.");
                    break;
                default:
                    System.out.println("Invalid choice.");
            }

        } while (choice != 3);

        sc.close();
    }
}

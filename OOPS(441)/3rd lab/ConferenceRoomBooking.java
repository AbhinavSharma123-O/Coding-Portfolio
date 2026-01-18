class ConferenceRoomBooking {
    static String[][] bookings = new String[10][4];
    static int count = 0;
    static void bookRoom(String date, int start, int end, String name) {
        for (int i = 0; i < count; i++) {
            if (bookings[i][0].equals(date)) {
                int bookedStart = Integer.parseInt(bookings[i][1]);
                int bookedEnd = Integer.parseInt(bookings[i][2]);
                if (start < bookedEnd && end > bookedStart) {
                    System.out.println("Room already booked");
                    return;
                }}}

        bookings[count][0] = date;
        bookings[count][1] = String.valueOf(start);
        bookings[count][2] = String.valueOf(end);
        bookings[count][3] = name;
        count++;
        System.out.println("Room booked successfully for " + name);}
    static void checkAvailability(String date, int start, int end) {
        for (int i = 0; i < count; i++) {
            if (bookings[i][0].equals(date)) {
                int bookedStart = Integer.parseInt(bookings[i][1]);
                int bookedEnd = Integer.parseInt(bookings[i][2]);
                if (start < bookedEnd && end > bookedStart) {
                    System.out.println("Room is NOT available.");
                    return;
                }
            }
        }

        System.out.println("Room is available.");
    }

    public static void main(String[] args) {
        bookRoom("10-02-2026", 10, 12, "Abhinav");
        bookRoom("10-02-2026", 12, 14, "Rayan");
        checkAvailability("10-02-2026", 11, 13);
        checkAvailability("10-02-2026", 14, 16);
    }
}

public class GreatCircle {
    public static void main(String[] args) {
        double lat1 = Double.parseDouble(args[0]);
        double lon1 = Double.parseDouble(args[1]);
        double lat2 = Double.parseDouble(args[2]);
        double lon2 = Double.parseDouble(args[3]);

        double r = 6371.0; // Earth radius in kilometers

        // convert degrees to radians
        double phi1 = Math.toRadians(lat1);
        double phi2 = Math.toRadians(lat2);
        double dphi = Math.toRadians(lat2 - lat1);
        double dlambda = Math.toRadians(lon2 - lon1);

        // haversine formula
        double sinHalfDphi = Math.sin(dphi / 2.0);
        double sinHalfDlambda = Math.sin(dlambda / 2.0);
        double h = sinHalfDphi * sinHalfDphi +
                   Math.cos(phi1) * Math.cos(phi2) * sinHalfDlambda * sinHalfDlambda;

        // clamp h into [0,1] without conditionals
        h = Math.max(0.0, Math.min(1.0, h));

        double centralAngle = 2.0 * Math.asin(Math.sqrt(h));
        double distance = r * centralAngle;

        // print with suffix required by grader
        System.out.println(distance + " kilometers");
    }
}

class DataTypesInfo {
    public static void main(String[] args) {

        byte b = 0;
        short s = 0;
        int i = 0;
        long l = 0L;
        float f = 0.0f;
        double d = 0.0;
        char c = '\u0000';
        boolean bool = false;

        System.out.println("byte: " + b + " Size: " + Byte.BYTES);
        System.out.println("short: " + s + " Size: " + Short.BYTES);
        System.out.println("int: " + i + " Size: " + Integer.BYTES);
        System.out.println("long: " + l + " Size: " + Long.BYTES);
        System.out.println("float: " + f + " Size: " + Float.BYTES);
        System.out.println("double: " + d + " Size: " + Double.BYTES);
        System.out.println("char: " + c + " Size: " + Character.BYTES);
        System.out.println("boolean: " + bool);
    }
}

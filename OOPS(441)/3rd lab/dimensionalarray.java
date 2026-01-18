public class dimensionalarray {
    
    public static void main(String[] args) {

        int[][][] marks = {
            {   
                {8, 9, 8},  
                {7, 8, 8}   
            },
            {   
                {9, 8, 9},  
                {7, 7, 7}   
            },
            {   
                {8, 8, 8},  
                {7, 8, 7}   
            }
        };
        for (int c = 0; c < marks.length; c++) {
            System.out.println("Class " + (c + 1) + ":");
            for (int s = 0; s < marks[c].length; s++) {
                System.out.print("  Student " + (s + 1) + ": ");
                for (int sub = 0; sub < marks[c][s].length; sub++) {
                    System.out.print(marks[c][s][sub] + " ");
                }
                System.out.println();
            }
        }
    }

}
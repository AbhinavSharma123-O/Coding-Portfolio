import java.util.ArrayList;
import java.util.Scanner; // Only need this once

public class ToDoList {
    public static void main(String[] args) {
        ArrayList<String> tasks = new ArrayList<>();
        Scanner scanner = new Scanner(System.in); // Initialize Scanner
        
        boolean isRunning = true; // Cleaner loop control

        while (isRunning) {
            System.out.println("\n--- TO-DO LIST ---"); // \n adds a blank line for looks
            System.out.println("1. Add Task");
            System.out.println("2. View Tasks");
            System.out.println("3. Remove Task");
            System.out.println("4. Exit");
            System.out.print("Enter choice: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // <--- CRITICAL: Eat the leftover 'Enter' key

            switch (choice) {
                case 1:
                    System.out.print("Enter task description: ");

                   
                    break;
                case 2:
                    System.out.println("Your Tasks:");
                    
                    
                    break;
                case 3:
                    System.out.println("Remove functionality coming soon...");
                    break;
                case 4:
                    isRunning = false; // Exit the loop
                    break;
                default:
                    System.out.println("Invalid choice.");
            }
        }
        scanner.close();
    }
}
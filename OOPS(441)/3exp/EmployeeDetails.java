import java.util.Scanner;

public class EmployeeDetails {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Loop to get details for 5 employees
        for (int i = 1; i <= 5; i++) {
            System.out.println("Employee " + i);

            System.out.print("ID: ");
            int id = sc.nextInt();

            // Crucial step: consume the leftover newline character
            sc.nextLine(); 

            System.out.print("Name: ");
            String name = sc.nextLine();

            System.out.print("Salary: ");
            double salary = sc.nextDouble();

            System.out.println("ID: " + id + ", Name: " + name + ", Salary: " + salary);
            
        }
        
        sc.close(); // Good practice to close the scanner
    }
}
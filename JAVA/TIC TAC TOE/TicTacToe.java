import java.util.Scanner;
import java.util.Stack;
import java.util.InputMismatchException; // Import the Exception

public class TicTacToe {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        char[][] gameboard = new char[3][3];
        initializeBoard(gameboard);
        
        Stack<int[]> moveHistory = new Stack<>();
        boolean gameEnded = false;
        char currentPlayer = 'X';

        System.out.println("Welcome to Tic-Tac-Toe!");
        System.out.println("Type 'undo' to take back a move.");

        while (!gameEnded) {
            printBoard(gameboard);
            System.out.print("Player " + currentPlayer + ", enter your move (row and column): ");
            
            String input = scanner.next();

            // --- UNDO CHECK ---
            if (input.equalsIgnoreCase("undo")) {
                if (undoLastMove(gameboard, moveHistory)) {
                    currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
                }
                continue;
            }

            // --- ROBUST INPUT HANDLING (The Interview Flex) ---
            int row, col;
            try {
                // 1. Try to parse the first word as an integer
                row = Integer.parseInt(input);
                // 2. Try to read the second number
                col = scanner.nextInt();
            } catch (NumberFormatException e) {
                // Catches if the first part wasn't a number (e.g. "apple")
                System.out.println("Invalid input! Please enter numbers (e.g. '1 1').");
                scanner.nextLine(); // Clear any remaining junk
                continue;
            } catch (InputMismatchException e) {
                // Catches if the second part wasn't a number
                System.out.println("Invalid input! Please enter numbers (e.g. '1 1').");
                scanner.nextLine(); // Clear the buffer
                continue;
            }

            int adjustRow = row - 1;
            int adjustCol = col - 1;

            if (isValidMove(gameboard, adjustRow, adjustCol)) {
                moveHistory.push(new int[]{adjustRow, adjustCol});
                placeMove(gameboard, adjustRow, adjustCol, currentPlayer);

                if (checkWinner(gameboard, currentPlayer)) {
                    printBoard(gameboard);
                    System.out.println("Player " + currentPlayer + " has won!");
                    gameEnded = true;
                } else if (isBoardFull(gameboard)) {
                    printBoard(gameboard);
                    System.out.println("It's a draw!");
                    gameEnded = true;
                } else {
                    currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
                }
            } else {
                System.out.println("Invalid move! Position taken or off board.");
            }
        }
        scanner.close();
    }

    // --- HELPER METHODS REMAIN THE SAME ---
    
    public static boolean undoLastMove(char[][] board, Stack<int[]> history) {
        if (history.isEmpty()) {
            System.out.println("No moves to undo!");
            return false;
        }
        int[] lastMove = history.pop();
        board[lastMove[0]][lastMove[1]] = '-';
        return true;
    }

    public static void initializeBoard(char[][] board) {
        for(int i = 0; i < board.length; i++) {
            for(int j = 0; j < board[i].length; j++) {
                board[i][j] = '-';
            }
        }
    }

    public static void printBoard(char[][] board) {
        System.out.println("-------------");
        for(int i = 0; i < board.length; i++) {
            System.out.print("| ");
            for(int j = 0; j < board[i].length; j++) {
                System.out.print(board[i][j] + " | ");
            }
            System.out.println();
            System.out.println("-------------");
        }
    }

    public static boolean isValidMove(char[][] board, int row, int col) {
        if (row < 0 || row >= board.length || col < 0 || col >= board[0].length) {
            return false;
        }
        return board[row][col] == '-';
    }

    public static void placeMove(char[][] board, int row, int col, char symbol) {
        board[row][col] = symbol;
    }

    public static boolean checkWinner(char[][] board, char symbol) {
        for (int i = 0; i < 3; i++) {
            if (board[i][0] == symbol && board[i][1] == symbol && board[i][2] == symbol) return true;
            if (board[0][i] == symbol && board[1][i] == symbol && board[2][i] == symbol) return true;
        }
        if (board[0][0] == symbol && board[1][1] == symbol && board[2][2] == symbol) return true;
        if (board[0][2] == symbol && board[1][1] == symbol && board[2][0] == symbol) return true;
        return false;
    }

    public static boolean isBoardFull(char[][] board) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == '-') return false;
            }
        }
        return true;
    }
}
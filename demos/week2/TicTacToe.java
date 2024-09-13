import java.util.*;

public class TicTacToe {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        char currentPlayer = 'O';
        int count = 0;
        char[] marks = {'0','1','2','3','4','5','6','7','8'};
        while(true){
            drawBoard(marks);
            if(winner(currentPlayer, marks)){
                System.out.printf("Player %s wins!", currentPlayer);
                return;
            }
            if(count == 9){
                System.out.println("It's a tie");
                return;
            }
            currentPlayer = currentPlayer == 'X' ? 'O' : 'X';
            int mark = promptForMark(currentPlayer, marks, scanner);
            marks[mark] = currentPlayer;
            count += 1;
        }
    }
    
    public static int promptForMark(char player, char[] marks, Scanner scanner){
        int mark = 0;
        while(true){
            try{
                System.out.printf("Player '%s', mark a spot: ", player);
                mark = scanner.nextInt();
            } catch(InputMismatchException e){
                System.out.println("Invalid choice");
                continue;
            } finally {
                scanner.nextLine();
            }
            if(marks[mark] == 'X' || marks[mark] == 'O'){
                System.out.println("That spot is taken");
            }
            else {
                break;
            }
        }
        return mark;
    }
    
    public static boolean winner(char player, char[] list){
        return (list[0] == player && list[1] == player && list[2] == player) ||
             (list[3] == player && list[4] == player && list[5] == player) ||
             (list[6] == player && list[7] == player && list[8] == player) ||
             (list[0] == player && list[3] == player && list[6] == player) ||
             (list[1] == player && list[4] == player && list[7] == player) ||
             (list[2] == player && list[5] == player && list[8] == player) ||
             (list[0] == player && list[4] == player && list[8] == player) ||
             (list[2] == player && list[4] == player && list[6] == player);
    }
    
    public static void drawBoard(char[] list){
        int count = 0;
        for(char el: list) {
            if(count < 2) {
                System.out.print(el + " | ");
                count += 1;
            } else {
                System.out.println(el);
                count = 0;
            }
        }
        System.out.println();
    }
}
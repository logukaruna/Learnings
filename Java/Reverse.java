import java.util.*;
public class Reverse {
    public static void main(String[] args) {
        System.out.println("Enter a number");
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();
        int rem = 0;
        while (num != 0) {
            rem = (rem * 10) + num % 10;
            num = num / 10;
        }
        System.out.println(rem);
        input.close();

        
    }
}

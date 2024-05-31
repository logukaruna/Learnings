import java.util.Scanner;

public class Palindrom {
    public static void main(String[] args) {
        System.out.print("Enter a Word:");
        Scanner input = new Scanner(System.in);
        String Word = input.nextLine().toLowerCase();
        int len = Word.length() - 1;
        String emt = "";
        for (int i = len; i >= 0; i--) {
            emt += Word.charAt(i);
        }
        System.out.println("Original: "+ Word);
        System.out.println("Reverse: " + emt);
        if (Word.equals(emt)) {
            System.out.println("The Given word is a palindrome");
        }
        else {
            System.out.println("The given word is not a palindrome");
        }
    }
}

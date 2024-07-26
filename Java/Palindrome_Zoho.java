import java.util.*;

public class Palindrome_Zoho {

    public static boolean isPali(String s) {
        String ogstr = s;
        String rev = "";
        int len = s.length();
        for (int i = len - 1; i >= 0; i--) {
            rev += s.charAt(i);
        }
        if (ogstr.equals(rev)) {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println("Enter a Sentence:");
        Scanner input = new Scanner(System.in);
        String sen = input.nextLine();
        String[] Words = sen.split(" ");
        String Output = "";

        for (String word : Words) {
            if (!isPali(word)) {
                Output += word + " " ;
            }

        }

        System.out.println("Output: " + Output);
        
    } 
    }


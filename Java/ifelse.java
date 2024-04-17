import java.util.*;

class ifelse {
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter your age:");
        int age = input.nextInt();
        if (age >= 18) {
            System.out.println("You are eligible to vote");
        }
        else {
            System.out.println("You are not eligible to vote");
        }
        
        System.out.println(age >=18 ? "You are eligible to vote" : "You are not eligible to vote");
    }
}
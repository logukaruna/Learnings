import java.util.*;

class Voter {
    public void Eligibility() {
        System.out.println("Enter your Age:");
        Scanner input = new Scanner(System.in);
        int Age = input.nextInt();
        if (Age >= 18) {
            System.out.println("You are Eiligible to vote...!!");
        } else {
            System.out.println("You are not Eligible to Vote...!!");
        }
    }

}

class PrintNumbers {
    public void Print() {
        System.out.println("Enter a number to Print from 0 to \"?\" ");
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();
        for (int i = 0; i < num; i++) {
            System.out.println(i);
        }
    }
}
    
class Claci {
    
    public int add(int n1, int n2){
        int r = n1 + n2;
        return r;
    }
}

public class classObject {
    public static void main(String[] args) {
        
        System.out.println("1) Voter Eligibility");
        System.out.println("2) Print Numbers");
        System.out.println("3) Claculator");
        System.out.println("Enter Tool Number:");
        Scanner input = new Scanner(System.in);
        int ch = input.nextInt();
        
        switch (ch) {
            case 1:
                Voter vote = new Voter();
                vote.Eligibility();
                break;
            case 2:
                PrintNumbers Print = new PrintNumbers();
                Print.Print();
                break;
            default:
                System.out.println("Invalid Option");

        }
    }
}

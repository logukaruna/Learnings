

public class Loops {
    public static void main(String[] args) {
        String s = "abca";
        int i = 0;
        int j = s.length()-1;
        while (i<=j) {
            if (s.charAt(i) == s.charAt(j)) {
                i++;
                j--;
                System.out.println("IF values");
                System.out.println(i);
                System.out.println(j);
            }
            else {
                System.out.println("else values");
                System.out.println(i);
                System.out.println(j);
                break;
            }
        }
    }
}

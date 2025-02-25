import java.util.*;

class romantoint {
    public static int romanToInt(String s) {
        HashMap<Character, Integer> set = new HashMap<>();
        set.put('I', 1);
        set.put('V', 5);
        set.put('X', 10);
        set.put('L', 50);
        set.put('C', 100);
        set.put('D', 500);
        set.put('M', 1000);

        int res = 0;

        for (char ch : s.toCharArray()) {
            if (set.containsKey(ch)) {
                res += set.get(ch);
            }
            else {
                return -1;
            }

        }

        return res;
    }

    public static void main(String[] args) {
        System.out.println("Enter Roman Letter");
        
        Scanner input = new Scanner(System.in);

        String s = input.nextLine();

        
        while (true) {
            int res = romanToInt(s);
            if (res == -1) {
                System.out.println("Invaild Roman Letter, Enter the Vaild Roman Letters");
            }
            else {

                System.out.println(res);

            }
            break;
        }
    }        

}
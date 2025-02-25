import java.util.*;



public class magicalnums {
    public static ArrayList<String> getBinaryNums(int n) {
        ArrayList<String> binarynumList = new ArrayList<>();

        for (int i = 1; i <= n; i++) {

            binarynumList.add(Integer.toBinaryString(i));
        }
        System.out.println(binarynumList);
        
        for (String s : binarynumList) {
            replace(s);
        }
        return binarynumList;
    }

    public static int getsum(ArrayList<String> bList) {
        int sum;

        return sum;
    }
    public static void main(String[] args) {
        System.out.println("Enter the range: ");
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        getBinaryNums(n);
    }
}
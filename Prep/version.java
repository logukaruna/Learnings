package Practice;
import java.util.*;

public class version {

    public static int vercheck(String V1, String V2) {
        int vnum1 = 0, vnum2 = 0;

        for (int i = 0, j = 0; (i < V1.length() || j < V2.length());) {

            while (i < V1.length() && V1.charAt(i) != '.') {
                vnum1 = vnum1 * 10 + (V1.charAt(i) - '0');
                i++;
            }
            while (j < V2.length() && V2.charAt(j) != '.') {
                vnum2 = vnum2 * 10 + (V2.charAt(j) - '0');
                j++;
            }

            if (vnum1 > vnum2) {
                return 1;
            }
            if (vnum2 > vnum1) {
                return -1;
            }
            vnum1 = vnum2 = 0;
            i++;
            j++;
        }
        return 0;
    }

    public static void main(String[] args) {
        System.out.println("Enter version 1: ");
        Scanner s = new Scanner(System.in);
        String V1 = s.nextLine();
        System.out.println("Enter version 2: ");
        String V2 = s.nextLine();

        if (vercheck(V1, V2) < 0) {
            System.out.println("Downgraded Version");
        } else if (vercheck(V1, V2) == 0) {
            System.out.println("Equal Version ");
        } else {
            System.out.println("Upgraded Version");
        }

    }

}

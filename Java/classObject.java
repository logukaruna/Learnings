class Claci {
    
    public int add(int n1, int n2){
        int r = n1 + n2;
        return r;
    }
}
public class classObject {

    public static void main(String[] args) {

        Claci c = new Claci();

        int r =    c.add(5, 8);
        System.out.println(r);
    }
}

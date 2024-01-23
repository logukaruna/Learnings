

public class linear {
    public static void main(String[] args) {

        int arr[] = { 25, 45, 65, 70, 76 };
        int traget = 65;
     //   int linearsearch = linearSearch(arr, traget);
     //   System.out.println("Element found at " + linearsearch);
        int binary = binarySearh(arr, traget, 0, arr.length - 1);
        System.out.println("Element found at " + binary);
    }
    
    public static int binarySearh(int[] arr, int traget, int left, int right) {
      
       if(left <= right){
           int mid = (left + right)/ 2;
           if (arr[mid] == traget) 
        {
            return mid;   
        }
        else if (arr[mid] < traget) {
           return binarySearh(arr, traget, left + 1, right);
        }
        else
        {
           return binarySearh(arr, traget, left, right - 1);
        }
       }
    return -1;

    }

    public static int linearSearch(int[] arr, int traget) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == traget) {
                return i;
            }

        }
        return -1;

    }
    


    
}
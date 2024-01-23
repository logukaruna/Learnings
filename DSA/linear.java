

public class linear {
    public static void main(String[] args) {

        int arr[] = { 25, 45, 65, 70, 76 };
        int traget = 45;
     //   int linearsearch = linearSearch(arr, traget);
     //   System.out.println("Element found at " + linearsearch);
        int binary = binarySearh(arr, traget);
        System.out.println("Element found at " + binary);
    }
    
    private static int binarySearh(int[] arr, int traget) {
       int left = 0;
       int right = arr.length - 1;
       while (left <= right){
           int mid = (left + right)/ 2;
           if (arr[mid] == traget) 
        {
            return mid;   
        }
        else if (arr[mid] < traget) {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
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
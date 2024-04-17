public class Bubble {
    public static void main(String[] args) {
        int arr[] = { 78, 65, 45, 98, 23, 45 };
        int len = arr.length;
        int temp = 0;


        System.out.println("Before Sorting");
        for (int nums : arr) {
            System.out.print(nums + " ");
        }
        
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len - i - 1; j++) { //Doing this len - i - 1 will help in reducing the time by not checking the last value of the array
                if (arr[j] > arr[j+1]) {
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j+1] = temp;
                }
                
            }
            
        }
        

        System.out.println();
        System.out.println("After Sorting");
        for(int nums : arr){
            System.out.print(nums + " ");
        }
    }
}

public class Selection {
    public static void main(String[] args) {
        int arr[] = { 34, 65, 72, 34, 12, 62, 23 };
        int temp = 0;
        int len = arr.length;
        int minIndex = -1;

        System.out.println("Before Sorting");
        for (int nums : arr) {
            System.out.print(nums + " ");
        }

        for (int i = 0; i < len - 1; i++) {
            minIndex = i;
            for (int j = i + 1; j < len; j++) {
                if (arr[minIndex] > arr[j]) {
                    minIndex = j;
                }
            }
            temp = arr[minIndex];
            arr[minIndex] = arr[i];
            arr[i] = temp;
        }
        System.out.println();
        System.out.println("After Sorting");
        for (int nums : arr) {
            System.out.print(nums + " ");
        }
    }
}

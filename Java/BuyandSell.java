import java.util.*;

public class BuyandSell {
    

    public static void main(String[] args) {
        int[] nums = { 7, 1, 5, 3, 6, 4 };
        int profit = 0;
        int buy = 0;
        int sell = 0;

        for (int i = 0; i < nums.length; i++) {
            if (buy >= nums[i]) { 
                buy = i;
            }
        }
        for (int j = buy; j < nums.length; j++) {
            if (nums[j] >= buy) {
                sell = j;
            }
        }
        profit = nums[buy] - nums[sell];
        System.out.println("Buy day: " + buy);
        System.out.println("Sell Day: "+ sell);
        System.out.println("Profit: " + profit);
    }
}

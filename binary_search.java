// problem  704
public class binary_search {
    public int search(int[] nums, int target) {
        int low = 0;
        int high = nums.length-1;
        int index = high/2;
        int current = nums[index];
        while (current != target) {
            if (low == high || low > high || high < low) {
                return -1;   
            }
            if (current > target) {
                high = index-1;
                index = index - (high - low)/2 -1;
            }
            else {
                low = index+1;
                index = index + (high - low)/2 +1;
            }
            if (low >= nums.length || high < 0) {return -1;}
            current = nums[index];
        }
        return index;
    }
    public static void main(String[] args) {
        binary_search sol = new binary_search();
        int[] nums = {2, 3};
        int target = 0;
        int res = sol.search(nums, target);
        System.out.println(res);
    }
}

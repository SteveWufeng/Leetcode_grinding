// problem  704
public class binary_search {
    public int search(int[] nums, int target) {
        int low = 0;
        int high = nums.length-1;
        int index = high/2;
        int current = nums[index];
        while (current != target) {
            if (current > target) {
                high = index-1;
                index = index - (high - low)/2 -1;
            }
            else {
                low = index+1;
                index = index + (high - low)/2 +1;
            }
            current = nums[index];
        }
        return index;
    }
    public static void main(String[] args) {
        binary_search sol = new binary_search();
        int[] nums = {-1,0,3,5,9,12};
        int target = 9;
        int res = sol.search(nums, target);
        System.out.println(res);
    }
}

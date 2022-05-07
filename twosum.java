import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int temp = target - nums[i];
            if (map.containsKey(temp)) {
                int[] result = {map.get(temp), i};
                return result;
            }
            map.put(nums[i], i);
        }
        return new int[0];
    }

    public static void main(String[] args) {
        int[] nums = {1,2,3,4,5,6};
        Solution solution = new Solution();
        int[] result = solution.twoSum(nums, 5);
        System.out.println(Arrays.toString(result));
    }
}
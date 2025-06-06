import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Map to store the complement and its index
        Map<Integer, Integer> numToIndex = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            
            // Check if the complement is already in the map
            if (numToIndex.containsKey(complement)) {
                return new int[] { numToIndex.get(complement), i };
            }
            
            // Store the current number and its index in the map
            numToIndex.put(nums[i], i);
        }
        
        // In case no solution is found, though the problem guarantees one
        throw new IllegalArgumentException("No two sum solution");
    }
}

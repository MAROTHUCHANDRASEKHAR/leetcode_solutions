class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1

        # Initialize variables to store the number of ways to reach the previous two steps.
        # ways_to_prev2 represents ways to reach step i-2
        # ways_to_prev1 represents ways to reach step i-1
        ways_to_prev2 = 1  # Corresponds to dp[0]
        ways_to_prev1 = 1  # Corresponds to dp[1]

        # Iterate from step 2 up to n
        for i in range(2, n + 1):
            # The number of ways to reach the current step 'i' is the sum of ways to reach
            # the previous two steps (i-1 and i-2).
            current_ways = ways_to_prev1 + ways_to_prev2

            # Update the previous values for the next iteration.
            ways_to_prev2 = ways_to_prev1
            ways_to_prev1 = current_ways

        # After the loop, ways_to_prev1 will hold the number of ways to reach step 'n'.
        return ways_to_prev1


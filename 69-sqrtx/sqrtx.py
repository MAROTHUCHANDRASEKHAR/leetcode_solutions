class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        low = 1
        high = x
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            # To avoid potential overflow with mid * mid, we can do mid <= x // mid
            # However, since x is an int and mid is int, mid * mid will fit in int for x up to 2^31 - 1
            # if mid > x // mid: # Equivalent to mid * mid > x
            if mid * mid > x:
                high = mid - 1
            else:
                ans = mid  # mid is a potential answer
                low = mid + 1
        return ans

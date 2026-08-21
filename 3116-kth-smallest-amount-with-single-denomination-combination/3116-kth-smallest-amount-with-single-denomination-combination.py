class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        # Precompute LCM for every subset
        lcms = []
        signs = []

        for mask in range(1, 1 << n):
            # Remove lowest set bit
            bit = mask & -mask
            i = bit.bit_length() - 1
            prev = mask ^ bit

            if prev == 0:
                curr_lcm = coins[i]
            else:
                prev_lcm = lcms[prev - 1]
                curr_lcm = prev_lcm // gcd(prev_lcm, coins[i]) * coins[i]

            lcms.append(curr_lcm)

            # Odd number of elements -> +
            # Even number -> -
            signs.append(1 if mask.bit_count() & 1 else -1)

        def count(x):
            ans = 0

            for lcm, sign in zip(lcms, signs):
                if lcm > x:
                    continue

                ans += sign * (x // lcm)

            return ans

        # kth smallest cannot exceed min(coins) * k
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
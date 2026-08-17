class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):

            # Current plot must be empty
            if flowerbed[i] == 0:

                # Check left neighbor
                left_empty = (i == 0 or flowerbed[i - 1] == 0)

                # Check right neighbor
                right_empty = (
                    i == len(flowerbed) - 1
                    or flowerbed[i + 1] == 0
                )

                # We can plant here
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1

                    # Planted enough flowers
                    if n == 0:
                        return True

        return n <= 0
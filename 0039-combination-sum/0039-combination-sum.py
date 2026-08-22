class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current, total):
            # We found a valid combination
            if total == target:
                result.append(current[:])
                return

            # Sum has become too large
            if total > target:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                # Choose num
                current.append(num)

                # i, NOT i + 1
                # because we can reuse the same number
                backtrack(i, current, total + num)

                # Undo the choice
                current.pop()

        backtrack(0, [], 0)

        return result
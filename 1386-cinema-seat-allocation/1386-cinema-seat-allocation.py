class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        for r, s in reservedSeats:
            rows.setdefault(r, set()).add(s)

        # Every completely empty row can accommodate 2 groups
        ans = (n - len(rows)) * 2

        for seats in rows.values():
            left = {2, 3, 4, 5}
            middle = {4, 5, 6, 7}
            right = {6, 7, 8, 9}

            can_left = not (seats & left)
            can_middle = not (seats & middle)
            can_right = not (seats & right)

            if can_left and can_right:
                # Two non-overlapping groups
                ans += 2
            elif can_left or can_middle or can_right:
                # At least one group can fit
                ans += 1

        return ans
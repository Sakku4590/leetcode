class Solution(object):
    def convert(self, s, num_row):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = [""]*num_row

        if num_row == 1 or num_row >= len(s):
            return s
            
        going_down = True
        current_row = 0

        for ch in s:
            
            rows[current_row] += ch
            
            if current_row == 0:
                going_down = True
            
            if current_row == (num_row - 1):
                going_down = False
                
            if going_down:
                current_row +=1
            else:
                current_row -= 1
            
        return "".join(rows)
            
        
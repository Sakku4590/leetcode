class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        A = []
        B = []
        
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    A.append((i, j))
                if img2[i][j] == 1:
                    B.append((i, j))
        
        if not A or not B:
            return 0
        
        count = defaultdict(int)
        best = 0
        
        for (ax, ay) in A:
            for (bx, by) in B:
                offset = (bx - ax, by - ay)
                count[offset] += 1
                if count[offset] > best:
                    best = count[offset]
        
        return best
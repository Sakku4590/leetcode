class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l=[]
        freq = {}
        for k,v in enumerate(list1):
            t = 0
            if v in list2:
                total = k + list2.index(v)
                freq[v] = freq.get(v,0) + total
                l.append(total)
        ans = []
        for i,j in freq.items():
            if j == min(l):
                ans.append(i)
        return ans
        
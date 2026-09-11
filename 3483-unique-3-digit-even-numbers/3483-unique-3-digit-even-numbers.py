class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        numbers = set()
        for a,b,c in permutations(digits, 3):
            if a == 0:
                continue
            if c % 2 != 0:
                continue
            
            number = a*100 + b*10 +c
            numbers.add(number)
        return(len(numbers))
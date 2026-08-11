class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)

        rank = {}

        for i, s in enumerate(sorted_scores):
            position = i + 1

            if position == 1:
                rank[s] = "Gold Medal"
            elif position == 2:
                rank[s] = "Silver Medal"
            elif position == 3:
                rank[s] = "Bronze Medal"
            else:
                rank[s] = str(position)

        return [rank[s] for s in score]
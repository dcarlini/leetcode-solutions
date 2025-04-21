class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        
        hidden = [lower]
        for i in range(len(differences)):
            hidden.append(hidden[i] + differences[i])
        
        return max(0, (upper - lower + 1) - (max(hidden) - min(hidden)))

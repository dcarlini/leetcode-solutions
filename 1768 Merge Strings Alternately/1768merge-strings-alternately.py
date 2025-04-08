class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = list(word1)
        w2 = list(word2)
        w3 = []

        p1 = 0
        p2 = 0

        while p1 < len(w1) and p2 < len(w2):
            w3.extend(w1[p1] + w2[p2])
            p1 += 1
            p2 += 1

        if p1 < len(w1):
            w3.extend(w1[p1:])
        elif p2 < len(w2):
            w3.extend(w2[p2:])

        return "".join(w3)






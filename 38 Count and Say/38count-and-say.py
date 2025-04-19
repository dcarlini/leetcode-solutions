class Solution:
    def countAndSay(self, n: int) -> str:

        s = "1"

        for i in range(n-1):
    
            rle = self.compress(s)
            s = self.concat(rle)

        return s



    def concat(self, l: list):
        s = ""

        for t in l:
            s += str(t[0]) + str(t[1])
        
        return s


    def compress(self, s: str):
        tuples = []
        c = None
        count = 0

        for l in s:
            if c is None:
                c = l
                count += 1
            elif l == c:
                count += 1
            else:
                tuples.append((count, int(c)))
                c = l
                count = 1

        if (count > 0):
            tuples.append((count,int(c)))

        return tuples


    
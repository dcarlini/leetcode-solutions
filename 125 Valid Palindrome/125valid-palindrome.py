class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        word = list(s)

        first = 0
        last = len(word) - 1

        while first < last :

            while first < last and not word[first].isalnum():
                first += 1

            while first < last and not word[last].isalnum():
                last -= 1

                
            # print("first", first, word[first])
            # print("last", last, word[last])

            if not word[first].lower() == word[last].lower():
                return False

            first += 1
            last -= 1



        return True

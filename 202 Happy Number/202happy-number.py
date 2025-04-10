class Solution:
    def isHappy(self, n: int) -> bool:
   
        # TODO: Write your code here
        slow = n
        fast = n

        while True:
            if slow == 1 or fast == 1:
                return True
            
            slow = self.computeSquares(slow)
            
            fast = self.computeSquares(fast)
            fast = self.computeSquares(fast)

            if slow == 1:
                return True

            if (slow == fast):
                return False
    


  
 
    def computeSquares (self, num):
        _sum = 0
        
        while (num > 0):
            digit = num % 10

            _sum += digit * digit
            num //= 10
        return _sum

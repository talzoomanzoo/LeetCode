class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)

        for j in range(len(x)):
            if list(x) == list(reversed(x)):
                pass
            else:
                return False
            
        return True
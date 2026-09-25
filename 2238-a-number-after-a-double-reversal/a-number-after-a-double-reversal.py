class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if (num>=0):
            value=int(str(int(str(num)[::-1]))[::-1])
        if (value==num):
            return True
        else:
            return False 

        
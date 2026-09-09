class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        freq={}
        count=0
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for num in nums:
            if target.startswith(num):
                remaining=target[len(num):]
                if remaining in freq:
                    count+=freq[remaining]
                if remaining==num:
                    count-=1
        return count

        




        
class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        stack=[]
        for i in range(len(nums)):
            while k>0 and stack and stack[-1]>nums[i]:
                stack.pop()
                k-=1
            stack.append(nums[i])
        stack=stack[:len(stack)-k]
        result="".join(stack).lstrip("0") 
        return result if result else "0"
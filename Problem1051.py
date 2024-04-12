class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        flag = 0
        for i, height in enumerate(heights):
            if height != expected[i]:
                flag += 1
        return flag
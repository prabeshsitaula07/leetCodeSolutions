class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        Intuition:
        Create a hasmap.
        Loop through nums and map the index to the number.
        '''
        myMap = {}
        for i, num in enumerate(nums):
            if num in myMap and abs(myMap[num] - i) <= k:
                    return True
            else:
                myMap[num] = i
        return False
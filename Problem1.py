class Solution:
    def twoSum(self, nums, target):
        num_map = {}  # Map to store number and its index

        # Iterate through the array
        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement exists in the map
            if complement in num_map:
                return [num_map[complement], i]

            # Store the number and its index in the map
            num_map[num] = i

        # If no solution found
        return None

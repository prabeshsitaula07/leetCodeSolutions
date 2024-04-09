class Solution:
    def findInMountainArray(self, target, mountain_arr):
        peak_index = self.find_peak(mountain_arr)

        asc_result = self.binary_search(mountain_arr, target, 0, peak_index, lambda x: x)

        if asc_result != -1:
            return asc_result

        desc_result = self.binary_search(mountain_arr, target, peak_index + 1, mountain_arr.length() - 1, lambda x: -x)

        return desc_result

    def find_peak(self, mountain_arr):
        left, right = 0, mountain_arr.length() - 1

        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        return left

    def binary_search(self, mountain_arr, target, left, right, key):
        target *= key(1)  # Adjust target according to whether we're searching in ascending or descending order

        while left <= right:
            mid = (left + right) // 2
            mid_val = mountain_arr.get(mid) * key(1)  # Adjust mid_val similarly

            if mid_val == target:
                return mid
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
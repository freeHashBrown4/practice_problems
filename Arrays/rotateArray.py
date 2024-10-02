#189. Rotate Array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        # Recalculate k to handle cases where k is greater than the length of nums
        k = k % len(nums)

        # Step 1: Rotate the entire array
        l = 0
        r = len(nums) - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        print(nums)  # After this step, the entire array is reversed

        # Step 2: Reverse the first k elements
        l = 0
        r = k - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        print(nums)  # After this step, the first k elements are reversed

        # Step 3: Reverse the remaining elements (from index k to the end)
        l = k
        r = len(nums) - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        print(nums)  # After this step, the remaining elements are reversed

# 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(nums):
    # Handle edge case: empty array
        if not nums:
            return 0
        
    # Initialize the 'slow' pointer (where to place next unique element)
        slow = 1
    
    # Use 'fast' pointer to scan through the array starting from index 1
        for fast in range(1, len(nums)):

        # If current element is different from previous element
            if nums[fast] != nums[fast - 1]:

            # Copy this unique element to the position tracked by 'slow'
                nums[slow] = nums[fast]
                
            # Increment 'slow' to prepare for next unique element
                slow += 1
    
    # 'slow' is now equal to the length of the array without duplicates
        return slow
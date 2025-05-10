#27. Remove Element
class Solution:
    def removeElement(nums, val):
        # Initialize a pointer for the position where non-val elements will be placed
        k = 0
    
    # Iterate through each element in the array
        for i in range(len(nums)):
            # If the current element is not the value we want to remove
            if nums[i] != val:
                # Place it at position k and increment k
                nums[k] = nums[i]
                k += 1
    
    # k now represents the length of the array without val elements
        return k
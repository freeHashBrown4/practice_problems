#27. Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        length = len(nums)

        #Check for edge cases, if the array is empty or only has one or two values in it

        l = 0
        r = length-1

        #Not sure if I should just change this to while true:
        #Need to put a while here instead of a for
        while (r >= l):

            #Keep on iterating l until the val is found
            if (nums[l] != val):
                l +=1

            #Keep on iterating r until non-val is found
            elif (nums[r] == val):
                r -=1

            else:
                #Do the swap
                nums[l] = nums[r]
                l +=1
                r -=1

        return l
                

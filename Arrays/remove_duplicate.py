# 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        #non-decreasing means increasing order, so ascending, 1234
        #Remove all the duplicated in num, 
        #Remember, the nums array or list is in ascending order,

        #[0,1,2,3,4,2,2,3,3,4]
        #         L
        #                 I R
        # [0, 1, 2, 3, 4, ________] and also return k, which is the number of unique values
        #Remember that we are trying to remove the duplicates,
        #So we use two pointers, we only do a swap with L and R, when K and R do
        #not equal each other 

        #We will not check the first value because it can't be a duplicate
        #So will start from the second

        length = len(nums)

        #Edge case
        #If nums array is less than 1,
        #this means there are no duplicates
        # if (nums < 1):
        #     #l will be the k
        #     return l

        #Define the two pointers called left and right
        l = 1
        r = 1
        
        # [1, 2 , 3]
        

        #We actually just need to go up to second last element, but including that element
        #We will get a index out range error
        #The R will check the last number
        for i in range(length-1):
            #We only do a swap if i and R do not equal each other
            #Swap the value in R with value in L
            if (nums[r] != nums[i]):
                nums[l] = nums[r]
                #Iterate l, once the swap is over
                l = l + 1
            #Other if the swaps or not
            #always iterate the i and r
            i = i + 1
            r = r + 1
    
        #The l will be the unique value
        return l


            
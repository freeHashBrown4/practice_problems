# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        #Input: Given the head of a linked list

        #Process: I can read all the values of the linked list to an array, then sort the array and then read back the values into another linked list

        #But that seems trivial, there must be a better way

        # I know that I can traverse through the linked list

        # All I have to do is traverse through the linked list, I can just change the direction of the each next. I know that each nodes next pointer points the next node in the singly linked list

        # All I have to do is change the direction

        #  None <- 1 <- 2 <- 3 <- 4 <- 5 -> None

        #                             Prev Curr

        # None <- 1 <- 2 <- 3 <- 4 <- 5

        # 5 -> 4 -> 3 -> 2 -> 1 -> None

        # I need the current node, but I also need the one after


        #Output: Return head of the linked list but the linked list needs to be reversed

        # Edge Case
        # Singly Linked List with one or zero nodes
        if not head or not head.next:
            return head


        #   None <- 1 <- 2 <- 3 <- 4 <- 5 -> None
        #                             prev. curr

        # Two pointers

        prev = None
        curr = head

        while curr != None:

            #Use temp to store curr.next
            temp = curr.next
            
            # Switch the arrows
            curr.next = prev

            # Iterate curr and prev
            prev = curr

            curr = temp
        
        return prev



        
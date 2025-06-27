# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        li = []
        curr = head
        while curr:
            li.append(curr)
            curr = curr.next
        left,right= 0,len(li)-1
        while left<right:
            li[left].next = li[right]
            left+=1

            if left==right:
                break
            li[right].next = li[left]
            right -= 1
        li[left].next = None

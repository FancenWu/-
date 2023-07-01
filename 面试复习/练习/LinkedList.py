class ListNode:
    def __int__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        dummy = ListNode(0)


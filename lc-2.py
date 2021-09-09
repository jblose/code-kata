#!/usr/bin/python3


from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def createLinkedList(self, l1):
        head = ListNode(val=l1[0])
        curr = head
        for x in range(1, len(l1)):
            curr.next = ListNode(val=l1[x])
            curr = curr.next
        return head


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def getNumber(lst):
            tens = 1
            res = 0

            for x in lst:
                res = res + (tens * x)
                tens = tens * 10
            return res

        def backToList(sumOfTwo):
            maxTens = len(str(sumOfTwo))
            lst = []
            for x in str(sumOfTwo):
                lst.append(int(x))
            lst.reverse()
            return lst

        sumOfTwo = getNumber(l1) + getNumber(l2)
        sumOfTwoList = backToList(sumOfTwo)
        return sumOfTwoList


# l1 = [9, 9]
# l2 = [1]

# l1 = [9, 9, 9, 9, 9, 9, 9]
# l2 = [9, 9, 9, 9]
print("WIP - 2021.09.08")
exit()
sol = Solution()
l1 = ListNode().createLinkedList([0, 1, 2])
l2 = ListNode().createLinkedList([3, 4, 5])
print(sol.addTwoNumbers(l1, l2))

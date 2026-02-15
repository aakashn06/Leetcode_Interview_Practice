# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Define necessary variables
        # Vals store values represented by lists
        # Power to multiply by 10 raised to necessary power
        # Traverser to traverse the lists
        val1 = 0
        val2 = 0
        power = 0
        traverser = l1

        # Get values from both lists
        while traverser is not None:
            val1 += traverser.val * (10 ** power)
            power += 1
            traverser = traverser.next
        power = 0
        traverser = l2
        while traverser is not None:
            val2 += traverser.val * (10 ** power)
            power += 1
            traverser = traverser.next
        
        # Compute sum and store as a string
        sum = val1 + val2
        sumString = str(sum)

        # Reverse the stored number
        reverseSumString = ""
        for digit in sumString:
            reverseSumString = digit + reverseSumString

        # Create new linked list to store the value and return it
        sumList = ListNode(int(reverseSumString[0]))
        i = 1
        traverser = sumList
        while i < len(sumString):
            traverser.next = ListNode(int(reverseSumString[i]))
            traverser = traverser.next
            i += 1
        return sumList
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        

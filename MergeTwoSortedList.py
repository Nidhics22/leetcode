class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        updated_list = new_list = ListNode(0)
        while list1 and list2:
            if list1.val <= list2.val:
                updated_list.next = list1
                list1 = list1.next
            else:
                updated_list.next = list2
                list2 = list2.next
            updated_list = updated_list.next
        if list1:
            updated_list.next = list1
        else:
            updated_list.next = list2
        return new_list.next
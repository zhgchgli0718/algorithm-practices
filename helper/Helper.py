class Helper:
    @staticmethod
    def listNode_to_array(head):
        array = []
        current = head
        count = 0
        while current:
            array.append(current.val)
            current = current.next
            count += 1
            if count >= 100:
                break
        return array
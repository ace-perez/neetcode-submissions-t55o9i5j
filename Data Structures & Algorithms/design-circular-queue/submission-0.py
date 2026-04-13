class LinkedNode:
    def __init__(self, val: int):
        self.val = val
        self.next = -1
        self.prev = -1

class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.curr_space = 0
        self.left = LinkedNode(-1)
        self.right = LinkedNode(-1)
        self.left.next = self.right
        self.right.prev = self.left
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        new_node = LinkedNode(value)
        tmp = self.right.prev
        new_node.next = self.right
        new_node.prev = tmp
        tmp.next = new_node
        self.right.prev = new_node

        self.curr_space += 1

        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        tmp = self.left.next
        tmp_next = tmp.next
        self.left.next = tmp_next
        tmp_next.prev = self.left

        self.curr_space -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        tmp = self.left.next
        
        return tmp.val
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        tmp = self.right.prev

        return tmp.val  


    def isEmpty(self) -> bool:
        if self.curr_space == 0:
            return True
        
        return False
        

    def isFull(self) -> bool:
        if self.curr_space == self.space:
            return True
        
        return False





# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
from linkedlist.list import ListNode, delete


class LinkedListStack:
    def __init__(self):
        self.peek: ListNode | None = None
        self.size: int = 0

    def size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def push(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.peek
        self.peek = node
        self.size += 1

    def peek(self) -> int:
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.peek.val

    def to_list(self) -> list:
        arr = []
        node = self.peek
        while node:
            arr.append(node.val)
            node = node.next
        arr.reverse()
        return arr

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        delete(self.peek)
        self.size -= 1


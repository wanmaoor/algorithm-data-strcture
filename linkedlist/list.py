class ListNode:
    """链表节点类"""

    def __init__(self, val: int):
        self.val: int = val  # 节点值
        self.next: ListNode | None = None  # 指向下一个节点的引用


# 初始化一个链表
# 1 - 3 - 2 - 5 - 4

n0 = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(5)
n4 = ListNode(4)

# 构建节点的引用
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4


# 插入一个节点
def insert(n: ListNode, p: ListNode):
    p.next = n.next
    n.next = p


n5 = ListNode(6)
insert(n1, n5)
print(n1.next.val)


# 删除一个节点
def delete(n: ListNode):
    n.next = n.next.next


delete(n1)
print(n1.next.val)

from typing import List, Any, Optional


class StaticArray:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        self._capacity = capacity
        self._data: List[Any] = [None] * capacity

    def set(self, index: int, value: Any) -> None:
        if not 0 <= index < self._capacity:
            raise IndexError("Index out of bounds.")
        self._data[index] = value

    def get(self, index: int) -> Any:
        if not 0 <= index < self._capacity:
            raise IndexError("Index out of bounds.")
        return self._data[index]


class DynamicArray:
    def __init__(self):
        self._capacity = 4
        self._size = 0
        self._data: List[Any] = [None] * self._capacity

    def _resize(self, new_capacity: int) -> None:
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def append(self, value: Any) -> None:
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = value
        self._size += 1

    def insert(self, index: int, value: Any) -> None:
        if not 0 <= index <= self._size:
            raise IndexError("Index out of bounds.")
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1

    def delete(self, index: int) -> None:
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds.")
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._data[self._size - 1] = None
        self._size -= 1
        if 0 < self._size < self._capacity // 4:
            self._resize(max(self._capacity // 2, 4))

    def get(self, index: int) -> Any:
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds.")
        return self._data[index]


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional['Node'] = None


class SinglyLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self._size = 0

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def insert(self, position: int, value: Any) -> None:
        if position < 0 or position > self._size:
            raise IndexError("Position out of bounds.")
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev = self.head
            for _ in range(position - 1):
                prev = prev.next
            new_node.next = prev.next
            prev.next = new_node
        self._size += 1

    def delete(self, value: Any) -> None:
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self._size -= 1
                return
            prev = current
            current = current.next
        raise ValueError(f"Value {value} not found in the list.")

    def find(self, value: Any) -> Optional[Node]:
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def print_list(self) -> None:
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" -> ".join(elements))

    def reverse(self) -> None:
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def get_head(self) -> Optional[Node]:
        return self.head

    def get_tail(self) -> Optional[Node]:
        if not self.head:
            return None
        current = self.head
        while current.next:
            current = current.next
        return current


class DoubleNode:
    def __init__(self, value: Any, next_node: Optional['DoubleNode'] = None, prev_node: Optional['DoubleNode'] = None):
        self.value = value
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:
    def __init__(self):
        self.head: Optional[DoubleNode] = None
        self.tail: Optional[DoubleNode] = None
        self._size = 0

    def append(self, value: Any) -> None:
        new_node = DoubleNode(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._size += 1

    def insert(self, position: int, value: Any) -> None:
        if position < 0 or position > self._size:
            raise IndexError("Position out of bounds.")
        new_node = DoubleNode(value)
        if position == 0:
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
                self.head = self.tail = new_node
        elif position == self._size:
            self.append(value)
            return
        else:
            current = self.head
            for _ in range(position):
                current = current.next
            previous = current.prev
            previous.next = new_node
            new_node.prev = previous
            new_node.next = current
            current.prev = new_node
        self._size += 1

    def delete(self, value: Any) -> None:
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self._size -= 1
                return
            current = current.next
        raise ValueError(f"Value {value} not found in the list.")

    def find(self, value: Any) -> Optional[DoubleNode]:
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def print_list(self) -> None:
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" <-> ".join(elements))

    def reverse(self) -> None:
        current = self.head
        self.head, self.tail = self.tail, self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev

    def get_head(self) -> Optional[DoubleNode]:
        return self.head

    def get_tail(self) -> Optional[DoubleNode]:
        return self.tail


class Queue:
    def __init__(self):
        self._items: List[Any] = []

    def enqueue(self, value: Any) -> None:
        self._items.append(value)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue.")
        return self._items.pop(0)

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("Peek from an empty queue.")
        return self._items[0]

    def is_empty(self) -> bool:
        return len(self._items) == 0


class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


class BinarySearchTree:
    def __init__(self):
        self.root: Optional[TreeNode] = None
        self._size = 0

    def insert(self, value: int) -> None:
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
        self._size += 1

    def _insert_recursive(self, node: TreeNode, value: int) -> None:
        if value < node.value:
            if node.left:
                self._insert_recursive(node.left, value)
            else:
                node.left = TreeNode(value)
        elif value > node.value:
            if node.right:
                self._insert_recursive(node.right, value)
            else:
                node.right = TreeNode(value)
        else:
            raise ValueError(f"Value {value} already exists in the tree.")

    def delete(self, value: int) -> None:
        self.root, deleted = self._delete_recursive(self.root, value)
        if deleted:
            self._size -= 1
        else:
            raise ValueError(f"Value {value} not found in the tree.")

    def _delete_recursive(self, node: Optional[TreeNode], value: int) -> (Optional[TreeNode], bool):
        if not node:
            return node, False
        deleted = False
        if value < node.value:
            node.left, deleted = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right, deleted = self._delete_recursive(node.right, value)
        else:
            deleted = True
            if not node.left and not node.right:
                return None, deleted
            elif not node.left:
                return node.right, deleted
            elif not node.right:
                return node.left, deleted
            else:
                successor = self._min_node(node.right)
                node.value = successor.value
                node.right, _ = self._delete_recursive(node.right, successor.value)
        return node, deleted

    def search(self, value: int) -> Optional[TreeNode]:
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node: Optional[TreeNode], value: int) -> Optional[TreeNode]:
        if not node:
            return None
        if value == node.value:
            return node
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder_traversal(self) -> List[int]:
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Optional[TreeNode], result: List[int]) -> None:
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def height(self) -> int:
        return self._height_recursive(self.root)

    def _height_recursive(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return 1 + max(left_height, right_height)

    def preorder_traversal(self) -> List[int]:
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node: Optional[TreeNode], result: List[int]) -> None:
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self) -> List[int]:
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node: Optional[TreeNode], result: List[int]) -> None:
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    def level_order_traversal(self) -> List[int]:
        result = []
        if not self.root:
            return result
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    def minimum(self) -> TreeNode:
        if not self.root:
            raise ValueError("Tree is empty.")
        return self._min_node(self.root)

    def _min_node(self, node: TreeNode) -> TreeNode:
        current = node
        while current.left:
            current = current.left
        return current

    def maximum(self) -> TreeNode:
        if not self.root:
            raise ValueError("Tree is empty.")
        return self._max_node(self.root)

    def _max_node(self, node: TreeNode) -> TreeNode:
        current = node
        while current.right:
            current = current.right
        return current

    def is_valid_bst(self) -> bool:
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True
            if not (low < node.value < high):
                return False
            return validate(node.left, low, node.value) and validate(node.right, node.value, high)
        return validate(self.root, float('-inf'), float('inf'))


def insertion_sort(lst: List[int]) -> List[int]:
    sorted_lst = lst.copy()
    for i in range(1, len(sorted_lst)):
        key = sorted_lst[i]
        j = i - 1
        while j >= 0 and sorted_lst[j] > key:
            sorted_lst[j + 1] = sorted_lst[j]
            j -= 1
        sorted_lst[j + 1] = key
    return sorted_lst


def selection_sort(lst: List[int]) -> List[int]:
    sorted_lst = lst.copy()
    n = len(sorted_lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if sorted_lst[j] < sorted_lst[min_idx]:
                min_idx = j
        sorted_lst[i], sorted_lst[min_idx] = sorted_lst[min_idx], sorted_lst[i]
    return sorted_lst


def bubble_sort(lst: List[int]) -> List[int]:
    sorted_lst = lst.copy()
    n = len(sorted_lst)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_lst[j] > sorted_lst[j + 1]:
                sorted_lst[j], sorted_lst[j + 1] = sorted_lst[j + 1], sorted_lst[j]
                swapped = True
        if not swapped:
            break
    return sorted_lst


def shell_sort(lst: List[int]) -> List[int]:
    sorted_lst = lst.copy()
    n = len(sorted_lst)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = sorted_lst[i]
            j = i
            while j >= gap and sorted_lst[j - gap] > temp:
                sorted_lst[j] = sorted_lst[j - gap]
                j -= gap
            sorted_lst[j] = temp
        gap //= 2
    return sorted_lst


def merge_sort(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst.copy()

    def merge(left: List[int], right: List[int]) -> List[int]:
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


def quick_sort(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst.copy()

    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

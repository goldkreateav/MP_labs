class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.height = 1
        self.left = None
        self.right = None

class Comparator:
    def __call__(self, a, b):
        return a < b

class AVLMap:
    def __init__(self, comparator=Comparator()):
        self.root = None
        self.comparator = comparator

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _rotate_right(self, y):
        x = y.left
        Y2 = x.right
        x.right = y
        y.left = Y2
        y.height = max(self._height(y.left), self._height(y.right)) + 1
        x.height = max(self._height(x.left), self._height(x.right)) + 1
        return x

    def _rotate_left(self, x):
        y = x.right
        X2 = y.left
        y.left = x
        x.right = X2
        x.height = max(self._height(x.left), self._height(x.right)) + 1
        y.height = max(self._height(y.left), self._height(y.right)) + 1
        return y

    def _get_balance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _insert(self, node, key, value):
        if not node:
            return Node(key, value)
        if self.comparator(key, node.key):
            node.left = self._insert(node.left, key, value)
        elif self.comparator(node.key, key):
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value
            return node

        node.height = max(self._height(node.left), self._height(node.right)) + 1
        return self._make_balance(node, key)

    def _make_balance(self, node, key):
        balance = self._get_balance(node)

        if balance > 1 and self.comparator(key, node.left.key):
            return self._rotate_right(node)

        if balance < -1 and self.comparator(node.right.key, key):
            return self._rotate_left(node)

        if balance > 1 and self.comparator(node.left.key, key):
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and self.comparator(key, node.right.key):
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _delete_node(self, node, key):
        if not node:
            return node
        if self.comparator(key, node.key):
            node.left = self._delete_node(node.left, key)
        elif self.comparator(node.key, key):
            node.right = self._delete_node(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self._delete_node(node.right, temp.key)

        if node is None:
            return node

        node.height = max(self._height(node.left), self._height(node.right)) + 1

        return self._make_balance(node, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if self.comparator(key, node.key):
            return self._search(node.left, key)
        return self._search(node.right, key)

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def delete(self, key):
        self.root = self._delete_node(self.root, key)

    def search(self, key):
        node = self._search(self.root, key)
        if node is None:
            raise KeyError(f'Ключ {key} не найден.')
        return node.value

    def update(self, key, value):
        node = self._search(self.root, key)
        if node is None:
            raise KeyError(f'Ключ {key} не найден.')
        node.value = value

    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, value):
        self.insert(key, value)

    def clear(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def __iter__(self):
        return self._in_order_traversal(self.root)

    def _in_order_traversal(self, node):
        if node:
            yield from self._in_order_traversal(node.left)
            yield (node.key, node.value)
            yield from self._in_order_traversal(node.right)


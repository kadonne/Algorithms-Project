# self_balancing_tree.py

class Node:
    def __init__(self, key, password):
        self.key = key
        self.password = password
        self.left = None
        self.right = None
        self.height = 1

class SelfBalancingTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _balance(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node):
        if node is not None:
            node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self._update_height(y)
        self._update_height(x)

        return x

    def _left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self._update_height(x)
        self._update_height(y)

        return y

    def insert(self, root, key, password):
        if root is None:
            return Node(key, password)

        if key < root.key:
            root.left = self.insert(root.left, key, password)
        else:
            root.right = self.insert(root.right, key, password)

        self._update_height(root)

        balance = self._balance(root)

        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self._right_rotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self._left_rotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def insert_key(self, key, password):
        self.root = self.insert(self.root, key, password)

    def search(self, root, key):
        if root is None:
            return None
        elif root.key == key:
            return root.key, root.password 

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def search_key(self, key):
        return self.search(self.root, key)

    def concatenate_values_recursive(self, node):
        result = ""
        if node:
            result += self.concatenate_values_recursive(node.left)
            result += str(node.key) + " "
            result += self.concatenate_values_recursive(node.right)
        return result

    def concatenate_values(self):
        return self.concatenate_values_recursive(self.root).strip()

    def print_values_recursive(self, node):
        if node:
            self.print_values_recursive(node.left)
            print(node.key, end=" ")
            self.print_values_recursive(node.right)

    def print_values(self):
        self.print_values_recursive(self.root)
        print()

    def print_tree_recursive(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.key))
            self.print_tree_recursive(node.left, level + 1, "L--- ")
            self.print_tree_recursive(node.right, level + 1, "R--- ")

    def print_tree(self):
        self.print_tree_recursive(self.root)

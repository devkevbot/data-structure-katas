from typing import Optional


class BSTNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class BST:
    """
    Binary Search Tree implementation.

    Invariants:
    - All nodes are either None or contain a unique integer value.
    - All nodes left of a parent node are strictly less than
    - All nodes right of a parent node are strictly greater than
    """

    def __init__(self) -> None:
        self.root = None

    def insert_recursive(self, val: int):
        """
        Inserts val into the BST.

        Let n be the number of nodes in the tree.
        Time: O(n) - In the worst case, the tree is completely vertical, meaning that all n nodes will
        have to be traversed.
        Space: O(n) - If the tree is completely vertical, the maximum recursiion depth will be n.
        """
        self.root = self.insert_recursive_helper(self.root, val)

    def insert_recursive_helper(self, root: Optional[BSTNode], val: int):
        if root is None:
            root = BSTNode(val)
            return root

        if val < root.val:
            root.left = self.insert_recursive_helper(root.left, val)
        else:
            root.right = self.insert_recursive_helper(root.right, val)

        return root

    def insert_iterative(self, val: int):
        """
        Inserts val into the BST.

        Let n be the number of nodes in the tree.
        Time: O(n) - In the worst case, the tree is completely vertical, meaning that all n nodes will
        have to be traversed.
        Space: O(1)
        """
        if self.root is None:
            self.root = BSTNode(val)
            return

        curr = self.root

        while curr is not None:
            if val < curr.val:
                if curr.left is None:
                    curr.left = BSTNode(val)
                    return
                curr = curr.left
            elif val > curr.val:
                if curr.right is None:
                    curr.right = BSTNode(val)
                    return
                curr = curr.right

    def inorder_traversal_recursive(self) -> list[int]:
        """
        Walks the tree in-order (Left -> Parent -> Right)

        Let n be the number of nodes in the tree.
        Time: O(n) - All nodes are visited
        Space: O(n) - If the tree is completely vertical, the maximum recursiion depth will be n.
        """
        path = []
        self.inorder_traversal_recursive_helper(self.root, path)
        return path

    def inorder_traversal_recursive_helper(
        self, root: Optional[BSTNode], path: list[int]
    ):
        if root is None:
            return

        self.inorder_traversal_recursive_helper(root.left, path)
        path.append(root.val)
        self.inorder_traversal_recursive_helper(root.right, path)

    def preorder_traversal_recursive(self) -> list[int]:
        """
        Walks the tree in-order (Parent -> Left -> Right)

        Let n be the number of nodes in the tree.
        Time: O(n) - All nodes are visited
        Space: O(n) - If the tree is completely vertical, the maximum recursiion depth will be n.
        """
        path = []
        self.preorder_traversal_recursive_helper(self.root, path)
        return path

    def preorder_traversal_recursive_helper(
        self, root: Optional[BSTNode], path: list[int]
    ):
        if root is None:
            return

        path.append(root.val)
        self.preorder_traversal_recursive_helper(root.left, path)
        self.preorder_traversal_recursive_helper(root.right, path)

    def postorder_traversal_recursive(self) -> list[int]:
        """
        Walks the tree in-order (Left -> Right -> Parent)

        Let n be the number of nodes in the tree.
        Time: O(n) - All nodes are visited
        Space: O(n) - If the tree is completely vertical, the maximum recursiion depth will be n.
        """
        path = []
        self.postorder_traversal_recursive_helper(self.root, path)
        return path

    def postorder_traversal_recursive_helper(
        self, root: Optional[BSTNode], path: list[int]
    ):
        if root is None:
            return

        self.postorder_traversal_recursive_helper(root.left, path)
        self.postorder_traversal_recursive_helper(root.right, path)
        path.append(root.val)

    def search_recursive(self, val: int) -> bool:
        """
        Searches for val in the BST.

        Let n be the number of nodes in the tree.
        Time: O(n) - In the worst case, the tree is completely vertical, meaning that all n nodes will
        have to be traversed.
        Space: O(n) - If the tree is completely vertical, the maximum recursiion depth will be n.
        """
        return self.search_recursive_helper(self.root, val)

    def search_recursive_helper(self, root: Optional[BSTNode], val: int) -> bool:
        if root is None:
            return False

        if val == root.val:
            return True

        if val < root.val:
            return self.search_recursive_helper(root.left, val)

        if val > root.val:
            return self.search_recursive_helper(root.right, val)

    def search_iterative(self, val: int) -> bool:
        """
        Searches for val in the BST.

        Let n be the number of nodes in the tree.
        Time: O(n) - In the worst case, the tree is completely vertical, meaning that all n nodes will
        have to be traversed.
        Space: O(1)
        """
        curr = self.root

        while curr is not None:
            if val == curr.val:
                return True

            if val < curr.val:
                curr = curr.left
            elif val > curr.val:
                curr = curr.right

        return False

    def delete_recursive(self, val: int):
        """
        Deletes val from the BST.

        Let n be the number of nodes in the tree.
        Time: O(n) - In the worst case, the tree is completely vertical, meaning that all n nodes will
        have to be traversed.
        Space: O(n) - If the tree is completely vertical, the maximum recursiion depth will be n.
        """
        self.root = self.delete_recursive_helper(self.root, val)

    def delete_recursive_helper(self, root: Optional[BSTNode], val: int):
        if root is None:
            return None

        if val == root.val:
            # No children
            if root.left is None and root.right is None:
                return None
            # Single child:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            successor = self.find_successor(root)
            root.val = successor.val
            root.right = self.delete_recursive_helper(root.right, successor.val)
        elif val < root.val:
            root.left = self.delete_recursive_helper(root.left, val)
        else:
            root.right = self.delete_recursive_helper(root.right, val)

        return root

    def find_successor(self, root: BSTNode):
        # Step right once, then go as left as possible
        curr = root.right
        while curr is not None and curr.left is not None:
            curr = curr.left
        return curr

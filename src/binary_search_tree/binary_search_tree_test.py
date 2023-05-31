from binary_search_tree import BST
import unittest


class TestBST(unittest.TestCase):
    def test_bst_insert_recursive(self):
        b = BST()
        b.insert_recursive(5)
        b.insert_recursive(3)
        b.insert_recursive(7)
        b.insert_recursive(2)
        b.insert_recursive(4)
        b.insert_recursive(6)
        b.insert_recursive(8)

        self.assertEqual(b.root.val, 5)

        self.assertEqual(b.root.left.val, 3)
        self.assertEqual(b.root.left.left.val, 2)
        self.assertEqual(b.root.left.right.val, 4)

        self.assertEqual(b.root.right.val, 7)
        self.assertEqual(b.root.right.left.val, 6)
        self.assertEqual(b.root.right.right.val, 8)

    def test_bst_insert_iterative(self):
        b = BST()
        b.insert_iterative(5)
        b.insert_iterative(3)
        b.insert_iterative(7)
        b.insert_iterative(2)
        b.insert_iterative(4)
        b.insert_iterative(6)
        b.insert_iterative(8)

        self.assertEqual(b.root.val, 5)

        self.assertEqual(b.root.left.val, 3)
        self.assertEqual(b.root.left.left.val, 2)
        self.assertEqual(b.root.left.right.val, 4)

        self.assertEqual(b.root.right.val, 7)
        self.assertEqual(b.root.right.left.val, 6)
        self.assertEqual(b.root.right.right.val, 8)

    def test_bst_inorder_traversal_recursive(self):
        b = BST()
        b.insert_recursive(5)
        b.insert_recursive(3)
        b.insert_recursive(7)
        b.insert_recursive(2)
        b.insert_recursive(4)
        b.insert_recursive(6)
        b.insert_recursive(8)

        self.assertListEqual(b.inorder_traversal_recursive(), [2, 3, 4, 5, 6, 7, 8])

    def test_bst_preorder_traversal_recursive(self):
        b = BST()
        b.insert_recursive(5)
        b.insert_recursive(3)
        b.insert_recursive(7)
        b.insert_recursive(2)
        b.insert_recursive(4)
        b.insert_recursive(6)
        b.insert_recursive(8)

        self.assertListEqual(b.preorder_traversal_recursive(), [5, 3, 2, 4, 7, 6, 8])

    def test_bst_postorder_traversal_recursive(self):
        b = BST()
        b.insert_recursive(5)
        b.insert_recursive(3)
        b.insert_recursive(7)
        b.insert_recursive(2)
        b.insert_recursive(4)
        b.insert_recursive(6)
        b.insert_recursive(8)

        self.assertListEqual(b.postorder_traversal_recursive(), [2, 4, 3, 6, 8, 7, 5])

    def test_bst_search_recursive(self):
        b = BST()
        b.insert_recursive(5)
        b.insert_recursive(3)
        b.insert_recursive(7)
        b.insert_recursive(2)
        b.insert_recursive(4)
        b.insert_recursive(6)
        b.insert_recursive(8)

        self.assertTrue(b.search_recursive(5))
        self.assertTrue(b.search_recursive(3))
        self.assertTrue(b.search_recursive(7))
        self.assertTrue(b.search_recursive(2))
        self.assertTrue(b.search_recursive(4))
        self.assertTrue(b.search_recursive(6))
        self.assertTrue(b.search_recursive(8))
        self.assertFalse(b.search_recursive(1))

    def test_bst_search_iterative(self):
        b = BST()
        b.insert_iterative(5)
        b.insert_iterative(3)
        b.insert_iterative(7)
        b.insert_iterative(2)
        b.insert_iterative(4)
        b.insert_iterative(6)
        b.insert_iterative(8)

        self.assertTrue(b.search_iterative(5))
        self.assertTrue(b.search_iterative(3))
        self.assertTrue(b.search_iterative(7))
        self.assertTrue(b.search_iterative(2))
        self.assertTrue(b.search_iterative(4))
        self.assertTrue(b.search_iterative(6))
        self.assertTrue(b.search_iterative(8))
        self.assertFalse(b.search_iterative(1))

    def test_bst_delete_recursive(self):
        b = BST()
        b.insert_recursive(5)
        b.insert_recursive(3)
        b.insert_recursive(7)
        b.insert_recursive(2)
        b.insert_recursive(4)
        b.insert_recursive(6)
        b.insert_recursive(8)

        # Delete root
        b.delete_recursive(5)

        self.assertEqual(b.root.val, 6)

        self.assertEqual(b.root.left.val, 3)
        self.assertEqual(b.root.left.left.val, 2)
        self.assertEqual(b.root.left.right.val, 4)

        self.assertEqual(b.root.right.val, 7)
        self.assertIsNone(b.root.right.left)
        self.assertEqual(b.root.right.right.val, 8)

        # Delete left-child leaf
        b.delete_recursive(2)
        self.assertIsNone(b.root.left.left)

        # Delete right-child leaf
        b.delete_recursive(8)
        self.assertIsNone(b.root.right.right)


if __name__ == "__main__":
    unittest.main()

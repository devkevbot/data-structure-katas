from trie import Trie

import unittest


class TestTrie(unittest.TestCase):
    def test_trie(self):
        t = Trie()
        t.insert("foobar")
        t.insert("mississippi")

        self.assertTrue(
            t.search_word("foobar"), "Expected to find word 'foobar' in Trie"
        )
        self.assertTrue(t.search_prefix("foo"), "Expected to find prefix 'foo' in Trie")
        self.assertFalse(
            t.search_prefix("fuzz"), "Expected not to find prefix 'fuzz' in Trie"
        )

        t.remove("foobar")
        self.assertFalse(
            t.search_word("foobar"), "Expected not to find word 'foobar' in Trie"
        )
        self.assertTrue(
            t.search_word("mississippi"), "Expected to find word 'mississippi' in Trie"
        )
        self.assertTrue(
            t.search_prefix("miss"), "Expected to find prefix 'miss' in Trie"
        )


if __name__ == "__main__":
    unittest.main()

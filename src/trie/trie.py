class TrieNode:
    def __init__(self) -> None:
        """
        A TrieNode represent a node in a Trie that contains pointers to its
        children and whether the node marks the termination of a word.
        """
        self.children = {}
        self.is_word = False


class Trie:
    """
    A Trie is a data structure typically used for finding prefixes and words.

    The space occupied by the Trie will be O(alphabet size * average word size * number of words)
    """

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Let k be the length of the word

        Time: O(k)
        Space: O(k)
        """
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.is_word = True

    def search_word(self, word: str) -> bool:
        """
        Let k be the length of the word

        Time: O(k)
        Space: O(1)
        """
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]

        return curr.is_word

    def search_prefix(self, prefix: str) -> bool:
        """
        Let k be the length of the word

        Time: O(k)
        Space: O(1)
        """
        curr = self.root

        for letter in prefix:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]

        return True

    def remove(self, word: str) -> None:
        """
        Let k be the length of the word

        Time: O(k)
        Space: O(1)

        NOTE: this implementation is NOT optimal since it does not clean up any nodes
        which may have only been part of the word to be deleted.
        """
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                return
            curr = curr.children[letter]

        if curr.is_word:
            curr.is_word = False

        if len(curr.children) == 0:
            curr = None

class TrieNode:
    def __init__(self):
        # initialize the end of word and also the prefix tree
        self.children = {}
        self.endofWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # first initialize a curr node 
        curr = self.root

        # check if the character is in the children
        for c in word:
            # if the character is not in the trie's children nodes
            if c not in curr.children:
                # then add that char at the children as a trie node
                curr.children[c] = TrieNode()
            # otherwise, also mark current to the current character 
            curr = curr.children[c]

        # otherwise, just add the char into the trie node 
        curr.endofWord = True 

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.endofWord # will be returning the boolean of there is a word or not

    def startsWith(self, prefix: str) -> bool:

        # check inside the prefix to see if the prefix matches and is there 

        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return True
        
        
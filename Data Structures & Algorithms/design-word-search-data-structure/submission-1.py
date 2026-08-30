class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c] 
        
        curr.endOfWord = True 

    def search(self, word: str) -> bool:
        curr = self.root

        # create a recursive function that checks whether character is '.' or just a normal character 
        def dfs(i, n):

            # meaning we have reached the end of list -> ending condition 
            if i == len(word):
                return n.endOfWord
    
            c = word[i]
            
            # check if the character s a period 
            if c == ".":
                for c in n.children.values():
                    # check all possible 
                    if dfs(i+1, c):
                        return True 
                    
                return False 

            # if its not a '.' then just check whether c is in the children  
            else:
                # check if the 
                if c not in n.children:
                    return False
                
                return dfs(i+1, n.children[c])
                            
        return dfs(0, self.root)  



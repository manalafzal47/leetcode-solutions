class Solution:
    def isValid(self, s: str) -> bool:
        # create stack
        stack = []
        hashmap = {"]":"[", "}":"{", ")":"("}

        # create brackets hashmap -> check if the 
        for char_s in s:
            # first condition: if the char is already in the hashmap
            if char_s not in hashmap:
                stack.append(char_s)

            # otherwise, if not, then check 
            else:
                if stack and stack[-1] == hashmap[char_s]:
                    stack.pop()
                
                else:
                    return False 
                    
        return True if not stack else False
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if (len(s)%2)!=0:
            return False
        
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if char == ')' :
                    if len(stack) == 0:
                        return False
                    if stack.pop() != '(':
                        return False
                elif char == '}':
                    if len(stack) == 0:
                        return False
                    if stack.pop() != '{':
                        return False
                elif char == ']':
                    if len(stack) == 0:
                        return False
                    if stack.pop() != '[':
                        return False
        
        if len(stack) == 0:
            return True
        else:
            return False
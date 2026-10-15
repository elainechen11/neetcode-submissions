class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'}': '{', ']': '[', ')':'('}
        stack = []
        for item in s:
            if item not in mapping:
                stack.append(item)
            else:
                if stack == []:
                    return False
                elif mapping[item] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack != []:
            return False
        return True


        
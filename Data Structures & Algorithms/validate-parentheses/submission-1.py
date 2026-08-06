class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(': ')', 
                '{': '}',
                '[': ']'}

        for bracket in s: 
            if bracket not in dic: 
                if not stack: 
                    return False
                elif dic.get(stack.pop()) == bracket:
                    continue
                else: 
                    return False
            else: 
                stack.append(bracket)

        return not stack
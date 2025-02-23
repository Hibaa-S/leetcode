class Solution(object):
    def isValid(self, s):
        dic = {")" : "(" , "]" : "[" , "}" : "{"}
        stack =[]

        for c in s:
            if c not in dic:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    pop = stack.pop()
                    if pop != dic[c]:
                        return False
        return not stack


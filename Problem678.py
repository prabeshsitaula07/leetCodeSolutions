class Solution:
    def checkStr(self, open_bracket, close_bracket, s):
        wildcards = open_brackets = 0
        
        for char in s:
            if char == open_bracket:
                open_brackets += 1
                
            elif char == close_bracket:
                if open_brackets:
                    open_brackets -= 1
                elif wildcards:
                    wildcards -= 1
                else:
                    return False
            else:
                wildcards += 1
        
        return open_brackets <= wildcards
        
    def checkValidString(self, s: str) -> bool:
        return self.checkStr('(', ')', s) and self.checkStr(')', '(', s[::-1])
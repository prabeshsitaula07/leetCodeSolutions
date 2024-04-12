class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0  # Pointer for name
        j = 0  # Pointer for typed

        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
            else:
                j += 1

        return i == len(name)
        
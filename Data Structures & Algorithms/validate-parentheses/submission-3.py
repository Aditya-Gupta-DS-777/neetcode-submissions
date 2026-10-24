
class Solution:
    def isValid(self, s: str) -> bool:
        sk = []
        p = {")": "(", "]": "[", "}": "{"}

        for y in s:
            if y == "(" or y == "{" or y == "[":
                sk.append(y)
            else:
                if not sk:
                    return False

                if sk[-1] == p[y]:
                    sk.pop()
                else:
                    return False

        if not sk:
            return True
        else:
            return False

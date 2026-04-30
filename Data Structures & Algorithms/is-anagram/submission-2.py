class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if both inputs are of different length then return false
        if len(s) != len(t):
            return False
        dict_1 = {}
        for char in s:
            dict_1[char] = dict_1.get(char, 0) + 1
        for char in t:
            dict_1[char] = dict_1.get(char, 0) - 1

        for c in dict_1:
            if dict_1.get(c) != 0:
                return False

        return True

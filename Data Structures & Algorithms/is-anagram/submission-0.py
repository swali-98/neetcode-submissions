class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if both inputs are of different length then return false
        if len(s) != len(t) :
            return False
        dict_1 =  {}
        for char in s:
            dict_1[char] = dict_1.get(char,0)+1
        dict_2 = {}
        for char in t:
            dict_2[char] =  dict_2.get(char,0)+1

        for c in dict_1:
            if dict_1.get(c) != dict_2.get(c):
                return False

        return True                

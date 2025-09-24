class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for i in magazine:
            if i in dict:
                dict[i]+=1
            else:
                dict[i] = 1
        for i in ransomNote:
            if i in dict and dict[i] > 0:
                dict[i] -= 1
            else:
                return False
        return True
        
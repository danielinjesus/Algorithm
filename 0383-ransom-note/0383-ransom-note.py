class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomNote2 = list(ransomNote)
        magazine2 = list(magazine)
        for i in range(len(ransomNote2)-1, -1, -1):
            for j in range(0, len(magazine2)):
                if ransomNote2[i] == magazine2[j]:
                    del ransomNote2[i]
                    del magazine2[j]
                    break
        if len(ransomNote2) > 0:
            return False
        else:
            return True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # probably a hashtable or map

        # for map it'll be key is the character, value is amount of times

        map1 = {}

        map2 = {}

        count = 1

        if len(s) != len(t):
            return False

        
        for char in s:
            if char in map1:
                map1[char] += 1
            else:
                map1[char] = 1

        for char in t:
            if char in map2:
                map2[char] += 1
            else:
                map2[char] = 1

        if map1 == map2:
            return True
        else:
            return False


            
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        

        final = ""

        for num in range (0, (max(len(word1), len(word2)))):
            
            if num < len(word1):
                final += word1[num]

            if num < len(word2):
                final += word2[num]

        return final
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        

        # check the first character in each word if they all match check the next

        # keep going till one doesn't match

        position = 0
        final = ""

        for char in strs[0]:

            for word in strs:

                if len(word) > position and char == word[position]:
                    None
                else:
                    return final

                
                   
            final += char 
            position += 1

        return final







        

                

                
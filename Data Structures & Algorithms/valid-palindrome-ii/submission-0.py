class Solution:
    def validPalindrome(self, s: str) -> bool:


        first = 0
        last = len(s) - 1

        def check(first, last):
            while first < last:
                if s[first].lower() == s[last].lower():
                    first += 1
                    last -= 1
            
                else:
                    return False

            return True

        
        while first < last:
            if s[first].lower() == s[last].lower():
                first += 1
                last -= 1
            
            else:
                if check(first + 1, last) or check(first, last - 1) == True:
                    return True
                
                else:
                    return False

            

        

        return True

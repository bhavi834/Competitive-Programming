class Solution:
    def gcdOfStrings(self, str1, str2):
        # Step 1: check if common pattern exists
        if str1 + str2 != str2 + str1:
            return ""
        
        # Step 2: custom gcd function (no import needed)
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # Step 3: return prefix of length = gcd(len1, len2)
        length = gcd(len(str1), len(str2))
        return str1[:length]
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                ch1, ch2 = s[l].lower(), s[r].lower()
                if ch1 != ch2:
                    return False
                l += 1
                r -= 1
        return True

        
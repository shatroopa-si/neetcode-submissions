class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Make into alphanumeric string
        s_an = ""
        for ch in s:
            s_an += ch.lower() if ch.isalnum() else ""

        # Check for palindrome
        i, n = 0, len(s_an)
        loop_until = (n / 2) - 1 if n % 2 == 0 else n // 2
        while i <= loop_until:
            ch1, ch2 = s_an[i], s_an[n - 1 - i]
            
            if ch1 != ch2:
                return False
            i += 1
        return True

        
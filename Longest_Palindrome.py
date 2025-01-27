def isPalindrome(s):
    return s == s[::-1]  # A string is a palindrome if it reads the same forwards and backwards

def longestPalindrome(s):
    longest = ""
    for i in range(len(s)):
        for j in range(i, len(s)):  # Check all substrings starting from index i
            substring = s[i:j + 1]  # Get the substring
            if isPalindrome(substring) and len(substring) > len(longest):
                longest = substring  # Update the longest palindrome
    return longest

# Example usage
print(longestPalindrome("babad"))  # Output: "bab" or "aba"
print(longestPalindrome("cbbd"))   # Output: "bb"
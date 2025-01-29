def longest_palindrome(s: str) -> str:
    def expand_around_center(left: int, right: int) -> str:
        # Expand around the center while the characters are the same
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the palindrome substring
        return s[left + 1:right]

    # Initialize the result as an empty string
    result = ""
    
    # Iterate through each character in the string
    for i in range(len(s)):
        # Case 1: Odd-length palindrome (center is a single character)
        odd_palindrome = expand_around_center(i, i)
        # Case 2: Even-length palindrome (center is two characters)
        even_palindrome = expand_around_center(i, i + 1)
        
        # Update the result with the longest palindrome found so far
        result = max(result, odd_palindrome, even_palindrome, key=len)
    
    return result

# Example usage
input_string = "babad"
print("Longest palindrome substring:", longest_palindrome(input_string))
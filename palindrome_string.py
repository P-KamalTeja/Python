"""
both for words and sentenses(not including symbols)
"""
a=input("Enter the string:-")
if(a==a[::-1]):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
"""
535 and its reverse is 535,so it is palindrome
"""

i=int(input("Enter the number:-"))
temp=i
rev=0
while(temp>0):
    rem=temp%10
    rev = rev*10+rem
    temp = temp//10
if(i==rev):
    print("It is a palindrome")
else:
    print("Not a Palindrome")
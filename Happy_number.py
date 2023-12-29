"""
Happy Number is sum of squares of number should leads to one.
"""

n=int(input("Enter the number:-"))
temp=0
while(temp!=1 and temp!=4 and temp!=n):
    temp=0
    while(n>0):
        rem=n%10
        temp += rem**2
        n=n//10
    n=temp
if(temp==1):
    print("It is a Happy Number")
else:
    print("It is not a Happy Number")
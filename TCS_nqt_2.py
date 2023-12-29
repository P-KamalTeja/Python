"""
Given no. is 541289101

find diff. of Odd placed integers and Even placed integers in given number

"""

n=int(input("Enter the number:-"))
temp=n
even=0
odd=0
count=0
while(temp>0):
    rem=temp%10
    count += 1
    if(count%2==0):
        even += rem
    else:
        odd += rem
    temp=temp//10
res=odd-even
print(res)
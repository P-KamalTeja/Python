"""
Strong Number

145= 1! + 4! + 5! == 145   --> 145 is Strong Number

"""

n=int(input("Enter the Number:-"))
num=n
sum=0
while(num>0):
    rem=int(num%10)
    fact=1
    if(rem==1 or rem==0):
        fact=1
    else: 
        for i in range(1,rem+1):
            fact=fact*i
    sum += fact
    num = num//10
print("Sum is:-",sum)
if(sum==n):
    print("It is a Strong Number")
else:
    print("It is not a Strong Number")
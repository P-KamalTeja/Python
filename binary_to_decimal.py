"""
8= 1 0 0 0
"""
n=int(input("Enter the number to convert binary to decimal:-"))
i,dec,base=0,0,1
temp=n
while(temp>0):    
    last_digit=temp%10
    dec += last_digit*base
    base *= 2
    temp = temp//10
print(dec)
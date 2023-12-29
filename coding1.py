"""
consider the following series: 0,0,2,1,4,2,6,3,8,4,10,5,-----------

we need to execute the program if the user enter n=10,we need to find 10th term in the series i.e; 9th term we need to get

"""

n=int(input("Enter the number:")) 
if(n<20001):
    if(n%2==0):
        c=(n-2)/2
        print("The number in the series is:",c)
    else:
        d=n-1
        print("The number in the series is:",d)
else:
    print("Enter the number less than 20000 only")
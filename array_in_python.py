from numpy import *
arr1 = array([1,2,3,4,5])
arr2 = array([1,2,3,4,5])
arr1 = arr1+5  #adds 5 to every element in arr1
print(arr1)
print(sum(arr1))
print(min(arr1))
print(max(arr1))
print(sort(arr1))
arr4=arr1
print(arr4)#Aliasing=id(Address) is copied in arr4 of arr1 address
arr5=arr1.view()#Shallow Copy=Diff. ID address and copy but change effects in arr5 if any change in arr1 occurs 
arr6=arr2.copy()#copy but change in arr2 doesn't effect on arr2(Diff. ID Address)
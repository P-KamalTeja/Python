from array import *
vals=array('i',[5,6,7,8,21])
print(vals)
print(vals.buffer_info())
for i in range (len(vals)):
    print(vals[i])
print()
for e in vals:
    print(e)
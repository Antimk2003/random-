a = []
s = int(input("enter the s value:"))
for i in range(s):
    val = int(input("enter the value:"))
    a.append(val)
    
max = 1 
for i in range(s):
    if (a[i]>max):
        max =a[i]
print("max value",max)  
min = max
for i in range(s):
     if (a[i]<min):
        min = a[i]
print ("min value",min)        
 
    
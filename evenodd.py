lst=[1,2,3,4,5,6,7,8,9]
odd=[]
even=[]

for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print("Odd",odd)
print("Even",even)

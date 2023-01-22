nk=input().split()
even=[]
odd=[]
for i in range(1,int(nk[0])+1):
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
nums=odd+even
print(nums[int(nk[1])-1])

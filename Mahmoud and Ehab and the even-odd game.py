n=int(input())
winner=""
for i in range(1,n+1):
    if(i%2==0):
        winner="Mahmoud"
    else:
        winner="Ehab"
print(winner)

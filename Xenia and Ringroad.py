nm=input().split()
tasks=list(map(lambda x: int(x),input().split()))
current_place=1
time=0
for x in tasks:
    if(x>current_place):
        time+=x-current_place
        current_place=x
    if(x<current_place):
        time+=int(nm[0])-current_place+x
        current_place=x
print(time)
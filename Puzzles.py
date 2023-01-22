#time limit
import itertools
nm=input().split()
lst=list(map(lambda x: int(x),input().split()))
a=list(itertools.combinations(lst,int(nm[0])))
main_dif=996
for x in a:
    dif=max(x)-min(x)
    if(dif<main_dif):
        main_dif=dif
print(main_dif)
#b=0
#for i in itertools.count(min(lst)):
#    if(i in lst):
#        b+=lst.count(i)
#    if(b==int(nm[0])):
#        c=i
#        break
#print(i-min(lst))

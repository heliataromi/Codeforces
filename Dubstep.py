import re
a=input()
a=re.sub("WUB"," ",a).split()
print(" ".join(a))
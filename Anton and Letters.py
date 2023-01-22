a=input()[1:-1].split(", ")
if("" in a):
    a.remove("")
print(len(set(a)))
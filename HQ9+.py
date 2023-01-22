p=input()
if('+' in p and '=' not in p and len(p)!=1):
    print('YES')
elif("H" in p or "Q" in p or "9" in p):
    print("YES")
else:
    print("NO")

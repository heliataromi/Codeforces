s = list(input())
a = []
for x in s:
	if x not in a and x in "hello":
		a.append(x)
print(a)
if ("l" in a):
	a.insert(a.index("l"), "l")
a = "".join(a)
if ("hello" in a):
	print("YES")
else:
	print("NO")

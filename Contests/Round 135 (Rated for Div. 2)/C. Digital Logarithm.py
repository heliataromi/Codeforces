def f(x):
    return len(str(x))


t = int(input())

for k in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if set(a) == set(b):
        print(0)
    else:
        ct = 0
        while set(a) != set(b):
            for num in a:
                if num in b:
                    a.remove(num)
                    b.remove(num)

            mx = max(a + b)
            if mx in a:
                a[a.index(mx)] = f(mx)
            else:
                b[b.index(mx)] = f(mx)
            ct += 1

        print(ct)

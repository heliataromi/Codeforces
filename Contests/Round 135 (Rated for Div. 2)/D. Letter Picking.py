t = int(input())

for k in range(t):
    s = input()
    alice = ''
    bob = ''
    for i in range(len(s)):
        if i % 2 == 0:
            if s[0] <= s[-1]:
                alice = s[0] + alice
                s = s[1:]
            else:
                alice = s[-1] + alice
                s = s[:len(s) - 1]

        else:
            if s[0] <= s[-1]:
                bob = s[0] + bob
                s = s[1:]
            else:
                bob = s[-1] + bob
                s = s[:len(s) - 1]

    if alice < bob:
        print('Alice')
    elif alice > bob:
        print('Bob')
    else:
        print('Draw')

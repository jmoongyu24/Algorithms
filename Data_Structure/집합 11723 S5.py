import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    command = input()
    if " " in command:
        cmd, num = command.split()
        num = int(num)
    else:
        cmd = command.strip()
        
    if cmd =="add":
        if num in S:
            continue
        else:
            S.add(num)
    elif cmd == "remove":
        if num in S:
            S.remove(num)
        else:
            continue
    elif cmd == "check":
        if num in S:
            print(1)
        else:
            print(0)
    elif cmd == "toggle":
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif cmd == "all":
        S.clear()
        S = set(range(1, 21))
    elif cmd == "empty":
        S.clear()
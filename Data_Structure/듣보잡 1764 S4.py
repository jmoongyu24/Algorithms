import sys
input = sys.stdin.readline

N, M = map(int, input().split())

listen = set()
look = set()

for _ in range(N):
    listen.add(input().strip())

for _ in range(M):
    look.add(input().strip())

result = list(listen & look)
result.sort()

print(len(result))
for member in result:
    print(member)
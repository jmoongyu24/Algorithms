N, M = map(int, input().split())

result = []
visited = [False] * N
num = list(map(int, input().split()))

num.sort()

def func(depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result.append(num[i])
            func(depth + 1)
            visited[i] = False
            result.pop()

func(0)
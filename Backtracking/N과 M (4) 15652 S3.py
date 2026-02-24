N, M = map(int, input().split())
result = []
visited = [False] * (N)

def func(depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(N):
        if len(result) == 0 or result[-1] <= i + 1:
            visited[i] = True
            result.append(i + 1)
            func(depth + 1)
            visited[i] = False
            result.pop()

func(0)
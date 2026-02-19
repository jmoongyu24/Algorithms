# 직전에 색칠한 색깔을 방문처리하는 식으로 코드 짤 필요 없음
# 현재 색칠할 색 3가지에 대해 다 살펴보는 식으로 단순하게 짤 수 있음
import sys
input = sys.stdin.readline

N = int(input())
cost = []

for _ in range(N):
    R, G, B = map(int, input().split())
    cost.append([R, G, B])

for i in range(1, N):
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]   # 빨간색 선택, 직전 색깔 초록&파랑 중 최솟값 택해서 더함
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1]   # 초록색 선택, 직전 색깔 빨강&파랑 중 최솟값 택해서 더함
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2]   # 파란색 선택, 직전 색깔 빨강&초록 중 최솟값 택해서 더함


print(min(cost[N-1][0], cost[N-1][1], cost[N-1][2]))

"""
import sys
input = sys.stdin.readline
inf = 987654321

N = int(input())
cost = [[-1, -1]]

for _ in range(N):
    R, G, B = map(int, input().split())
    cost.append([[R, 1], [G, 2], [B, 3]])

dp = [inf] * 1001
visited = [False] * 3

dp[1] = min(cost[1])
visited[cost[1].index(dp[1])] = True

for i in range(2, N + 1):
    chk = 0
    for j in range(3):
        if visited[j]:
            chk = j
    for j in range(3):
        if not visited[j]:
            dp[i] = min(dp[i], dp[i - 1] + cost[i][j][0])
        color_index = [color[1] for color in cost[i]]
        visited[color_index.index(cost[i][j][1])] = True
    visited[chk] = False

print(dp)
"""
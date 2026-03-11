import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
dp = [0] * N
dp[0] = nums[0]

for i in range(1, N):
    dp[i] = nums[i] + dp[i-1]

for _ in range(M):
    i, j = map(int, input().split())
    if i==1:
        result = dp[j-1]
    else:
        result = dp[j-1] - dp[i-2]
    print(result)
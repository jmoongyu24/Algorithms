N = int(input())
A = list(map(int, input().split()))
dp = [1] * 1001

dp[1] = 1

for i in range(1, N):
    for j in range(0, i):
        # i 이전의 수를 순회하면서 A[i]보다 작은 수 A[j]가 있을 경우, dp[i]는 그대로 쓰거나 위치 j의 dp[j] 값에 현재 위치의 수 1을 추가해 큰 값을 저장 
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
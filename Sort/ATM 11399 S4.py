N = int(input())
times = list(map(int, input().split()))
times.sort()

time_person = [0] * 1001

if N > 1:
    time_person[0] = times[0]
    for i in range(1, N):
        time_person[i] = time_person[i - 1] + times[i]
    result = sum(time_person)
else:
    result = times[0]

print(result)
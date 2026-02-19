st = input()
length = len(st)
result = set()

for window_size in range(1, len(st) + 1):
    for i in range(length - window_size + 1):
        result.add(st[i:i + window_size])

print(len(result))
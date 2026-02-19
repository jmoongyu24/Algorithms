import sys
input = sys.stdin.readline

N = int(input())
string = set()

for _ in range(N):
    st = input().strip()
    string.add((st, len(st)))

string = sorted(string, key = lambda x: (x[1], x[0]))

for word, _ in string:
    print(word)
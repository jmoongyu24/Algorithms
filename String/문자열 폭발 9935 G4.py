"""
1. 첫문자가 폭탄과 동일, 해당 위치부터 폭탄 길이만큼 문자열 비교
2. 일치하는 부분 '-'로 대체 후 끝까지 탐색, 카운트 1증가
3. - 있는 부분 모두 제거
4. 1~3 반복
5. 더 이상 폭발할 수 없는 경우(카운트 0인 경우) 종료
6. 남아있는 문자 있으면 출력, 없으면 프룰라 출력
"""

"""
# while문으로 인한 시간 초과

while True:
    count = 0
    positions = []
    
    for i in range(len(string)-len(bomb)+1):
        if string[i:i+len(bomb)] == bomb:
            count += 1
            positions.append(i)

    if count == 0:
        break
    
    string = list(string)
    for position in positions:
        for i in range(position, position + len(bomb)):
            string[i] = '-'
    string = ''.join(string)
    string = string.replace('-', '')
    
if len(string)==0:
    print("FRULA")
else:
    print(string)
"""
string = input().strip()
bomb = input().strip()

bomb_len = len(bomb)

stack = []

for char in string:
    stack.append(char)
    
    # stack[len(stack)-bomb_len:]: bomb 문자열
    if ''.join(stack[len(stack)-bomb_len:]) == bomb:
        del stack[len(stack)-bomb_len:]

result = ''.join(stack)

if len(result) == 0:
    print("FRULA")
else:
    print(result)
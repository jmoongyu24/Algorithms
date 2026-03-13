from collections import deque

"""
1. 트럭 1대 다리에 추가
2. 트럭 1대 다음 다리 위치로 이동 후 다음 트럭 조건 확인
3. 올라갈 트럭의 무게와 현재 다리에 있는 트럭들의 무게 합해서 L과 비교, 트럭 개수 총합이 w보다 작은지 확인
4. 모든 트럭이 이동 완료할때까지 반복
"""

n, w, L = map(int, input().split())
q_truck = deque(list(map(int, input().split())))
q_bridge = deque([0] * w)
time = 0
bridge_weight = 0

# 트럭이 아직 남았거나 다리에 트럭이 남아있는 동안 반복
while q_truck or bridge_weight > 0:
    time += 1

    # 다리에서 트럭 나감
    # 무게가 0인 것도 나감 = 빈 공간임. 그냥 트럭 이동만
    # rotate 효과: 다리 위 트럭이 한 칸씩 이동, 맨 앞 트럭은 나감
    out_truck = q_bridge.popleft()
    bridge_weight -= out_truck

    # 다리에 트럭을 올릴 수 있는지 확인
    if q_truck:
        cur_truck = q_truck[0]

        # 현재 다리 위 트럭 무게 총합 + 새 트럭 무게 <= L이면 올림
        if bridge_weight + cur_truck <= L:
            q_bridge.append(cur_truck)
            bridge_weight += cur_truck
            q_truck.popleft()  # 트럭 올라감
        else:
            q_bridge.append(0)  # 트럭이 올라갈 수 없으면 빈 공간 추가 = 트럭 이동 기능

print(time)
"""

2872 - 우리집엔 도서관이 있어

사전순으로 정렬한다 하였지만 책 번호가 이미 사전순으로 매겨져있다.
이 책 번호를 오름차순 정렬하는 문제이다.
N의 범위가 300,000 이하이며 시간제한이 1초이므로 O(N^2)는 불가.

(3, 2, 1) 초기 순서
(2, 3, 1) 2번을 옮긴 후
(1, 2, 3) 1번을 옮긴 후

---
문제를 제대로 읽지않아서 다시 풀었다.
책은 항상 위로 쌓아야 한다는 것을... 왜 꽂는다고 생각했지?

먼저 임의의 책을 어느걸로 옮기는지가 중요할 것 같은데
어차피 책은 위로 쌓으므로, 임의의 책을 정하는 것 보다 가장 마지막 번호가 있는 책의 위치를 찾고
내림차순으로 target을 확인하며 교환 횟수를 count

"""
import sys
input = sys.stdin.readline

n = int(input()) # 책의 개수 n 이자 책의 마지막 번호가 되는 변수
arr = [int(input()) for i in range(n)] # 가장 위에 있는 책부터 아래에 있는 책까지 순서대로 주어진다.

max_num = arr.index(max(arr)) # 가장 마지막 번호의 책이 어느 인덱스에 있는지 찾는다.
result = n # 마지막 책 번호

for i in range(max_num, -1, -1): # max_num 부터 0까지 -1 반복
    if arr[i] == result : # 1) 만약 확인하는 arr[i]가 마지막 번호의 책과 같은 경우
        result -= 1 # 마지막번호부터 내림차순으로 찾기 (옮긴 횟수 count-1)

print(result) # 정답 출력

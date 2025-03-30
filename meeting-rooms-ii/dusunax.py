'''
# 253. Meeting Rooms II

최소 힙 Min Heap을 사용하여 회의 종료 시간을 저장합니다. 최소 힙의 길이는 필요한 회의실 개수입니다.

## 개념
```
💡 최소 힙 Min Heap
- 힙은 완전 이진 트리이다.
- 부모 노드의 값이 자식 노드의 값보다 작다.
- 최소값을 루트에 두기 때문에 최소값을 찾는 시간복잡도가 O(1)이다.
```
```
💡 완전 이진 트리
- 트리의 모든 레벨이 완전히 채워져 있고, 마지막 레벨은 왼쪽부터 채운다.
- 삽입과 삭제는 O(log n)의 시간복잡도를 가진다.
  - 삽입은 트리의 마지막 노드에 삽입하고 버블업을 진행한다.
  - 삭제는 트리의 루트 노드를 삭제하고, 버블다운을 진행한다.
```

## 회의실 재사용 조건
가장 먼저 끝나는 회의와 다음 회의 시작을 비교하여, 다음 회의 시작이 가장 먼저 끝나는 회의보다 크거나 같다면, 같은 회의실을 사용 가능하다.

## 풀이
```
최소 힙의 길이 = 사용 중인 회의실 개수 = 필요한 회의실 개수
```
1. 회의 시작 시간을 기준으로 정렬
2. 회의 배열을 순회하며 회의 종료 시간을 최소 힙에 저장
3. 회의실을 재사용할 수 있는 경우, 가장 먼저 끝나는 회의 삭제 후 새 회의 종료 시간 추가(해당 회의실의 종료 시간 업데이트)
4. 최종 사용 중인 회의실 개수를 반환

## 시간 & 공간 복잡도

### TC is O(n log n)
- 회의 배열 정렬: O(n log n)
- 회의 배열 순회: O(n)
- 최소 힙 삽입 & 삭제: O(log n)

### SC is O(n)
- 최소 힙: 최악의 경우 O(n)
'''
from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        min_heap = [] 
        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heappop(min_heap)
            
            heappush(min_heap, interval.end)
        
        return len(min_heap)

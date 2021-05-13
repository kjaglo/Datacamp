from collections import deque

queue = deque([3, 4, 5])  # deque([3, 4, 5])
print(queue)  # deque([3, 4, 5])
queue.append(6)  # deque([3, 4, 5, 6])
print(queue)  # deque([3, 4, 5, 6])
print(queue.popleft())  # 3
print(queue)  # deque([4, 5, 6])

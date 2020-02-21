# uing List
'''
queue=[]
queue.append('a')
queue.append('b')
queue.append('c')
queue.append('d')
print(queue)
queue.pop(0)
queue.pop(0)
queue.pop(0)
print(queue)
'''


# using collection deque
'''
from _collections import deque
x=deque()
x.append('a')
x.append('b')
x.append('c')
x.append('d')
x.append('e')
print(x)
print(x.popleft())
print(x.popleft())
print(x.popleft())
print(x.popleft())
print(x)

'''

# using queue.queue method

from queue import Queue
q = Queue(maxsize=3)
print(q.qsize())
q.put('a')
q.put('b')
q.put('c')
print("\nFull: ", q.full())
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
print("\nEmpty: ", q.empty())

q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())
 print(q.get())

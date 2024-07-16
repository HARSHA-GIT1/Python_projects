"""
In This Program We Use The Queue Class And Check Its Functions Work or Not
"""
from Making_Queue import *
queue = Queue()
"""print(queue.Head)
print(queue.Tail)"""
queue.enqueue(12)
queue.enqueue(13)
queue.enqueue(14)
queue.enqueue(15)
queue.enqueue(16)
queue.enqueue(17)
queue.enqueue(18)
queue.enqueue(19)
queue.enqueue(20)
queue.enqueue(21)

print(queue)

queue.dequeue()
print(queue)

print(len(queue))

queue.peek()
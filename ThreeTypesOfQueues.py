import queue


q = queue.Queue()
q.put(400)
q.put(100)
q.put(500)
q.put(50)

while not q.empty():
    print(q.get(), end=' ')

print()
#LIFO

lq = queue.LifoQueue()
lq.put(400)
lq.put(100)
lq.put(500)
lq.put(50)

while not lq.empty():
    print(lq.get(), end=' ')

print()
#Priority Queue

pq = queue.PriorityQueue()
pq.put(400)
pq.put(100)
pq.put(500)
pq.put(50)

while not pq.empty():
    print(pq.get(), end=' ')

print()
#Priority Queue

pq = queue.PriorityQueue()
pq.put((400, 'John'))
pq.put((100,'Maria'))
pq.put((500, 'Frank'))
pq.put((50, 'Mavi'))

while not pq.empty():
    #print(pq.get(), end=' ')
    print(pq.get()[1], end=' ')
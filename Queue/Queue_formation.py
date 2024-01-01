queue = []

queue.append('g')
queue.append('f')
queue.append('g')

print('Initial queue')
print(queue)

print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)
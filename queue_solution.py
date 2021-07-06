from queue import Queue

# Initializing a queue
problem_queue = Queue(maxsize = 9)

# Return Boolean for Empty Queue
print("\nIs the queue Empty? ", problem_queue.empty())

# Adding of element to queue
problem_queue.put(21)
problem_queue.put(18)
problem_queue.put(5)
problem_queue.put(70)
problem_queue.put(14)

# Return Boolean for Full Queue.
print("\nIs the queue Full? ", problem_queue.full())

# Removing element from queue twice
print("\nElements dequeued from the queue:")
print(problem_queue.get())
print(problem_queue.get())

# Add 4 more elements to the queue 
problem_queue.put(2)
problem_queue.put(12)
problem_queue.put(36)
problem_queue.put(11)

# Return Boolean for Full Queue
print("\nIs the queue Full? ", problem_queue.full())
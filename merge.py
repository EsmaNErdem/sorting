def merge(lst1, lst2):
    a, b = 0, 0
    output = []
    while a < len(lst1) and b < len(lst2):
        if lst1[a] <= lst2[b]:
            output.append(lst1[a])
            a += 1
        else:
            output.append(lst2[b])
            b += 1

    while a < len(lst1):
        output.append(lst1[a])
        a += 1
    while b < len(lst2):
        output.append(lst2[b])
        b += 1

    return output

# print(merge([1,2,3,4,5], [6,7,8,9]))
# print(merge([1,2,3,4,5], [1,2,6,7,8,9]))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2 
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


print(merge_sort([4, 20, 12, 10, 7, 9]))






import heapq

def dijkstra(graph, source):
    distances = {}  # Dictionary to store the shortest distances
    queue = [(0, source)]  # Priority queue to track the vertices and their distances
    visited = set()  # Set to track the visited vertices

    # Initialize distances to infinity except for the source vertex
    for vertex in graph:
        distances[vertex] = float('inf')
    distances[source] = 0

    while queue:
        # Pop the vertex with the smallest distance from the queue
        current_distance, current_vertex = heapq.heappop(queue)

        # Skip if the vertex has already been visited
        if current_vertex in visited:
            continue

        # Mark the current vertex as visited
        visited.add(current_vertex)

        # Update distances of neighboring vertices
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances



import heapq

# Create an empty list to serve as the heap
heap = []

# Insert elements into the heap (negated)
heapq.heappush(heap, -10)
heapq.heappush(heap, -5)
heapq.heappush(heap, -15)

# Retrieve elements from the heap (negated)
max_element = -heapq.heappop(heap)
print(max_element)  # Output: 15


# dynamic programming is to solve the subproblems in a bottom-up manner, starting from the simplest subproblems and gradually building up to solve larger and more complex subproblems. The solutions to the subproblems are stored in a table or array, known as a memoization table, so that they can be looked up and reused when needed.

def fibonacci_of(n):
    if n in {0, 1}:  # Base case
        return n
        return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case

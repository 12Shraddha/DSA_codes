import heapq
arr=[1,5,7,9,8,3]
K=5
pq = []
heapq.heapify(pq)

for i in range(len(arr)):

    # Insert elements into
    # the priority queue
    heapq.heappush(pq, arr[i])

    # If size of the priority
    # queue exceeds k
    if (len(pq) > K):
        heapq.heappop(pq)
print(pq)
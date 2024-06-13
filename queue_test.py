from priority_queue import PriorityQueue

def main():
    pq = PriorityQueue()

    pq.push(10)
    pq.push(20)
    pq.push(5)

    print(f"Size of priority queue: {pq.size()}")
    print(f"Top element: {pq.top()}")

    while not pq.empty():
        print(f"Removing top element: {pq.pop()}")

if __name__ == "__main__":
    main()

class Queue():

    def __init__(self, max_size, queue=[]):
        self.max_size = max_size
        self.queue = queue

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        self.queue = self.queue[1:]

    def top(self):
        print(f"First element in queue is {self.queue[0]}")

    def isFull(self):
        if len(self.queue) == self.max_size:
            print("size of stack is full")

    def isEmpty(self):
        if len(self.queue) == 0:
            print("Size of stack is Empty.")

    def print_queue(self):
        print(self.queue) 


queue = Queue(max_size=3, queue=[])
queue.isEmpty()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.isFull()
queue.print_queue()
queue.dequeue()
queue.enqueue(60)
queue.print_queue() 
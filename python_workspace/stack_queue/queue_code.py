class Queue():

    def __init__(self, queue = None):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        self.queue = self.queue[1:]

    def print_queue(self):
        print(self.queue)
        
    def first(self):
        print("First Element is : ", self.queue[0]) 

    def is_empty(self):
        if len(self.queue) == 0:
            print("queue is empty")
        else:
            print("length of queue is ", len(self.queue)) 


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.print_queue()
queue.first()
queue.dequeue()
queue.print_queue()
queue.is_empty()
queue.dequeue() 
queue.print_queue()
queue.first()
queue.dequeue()
queue.print_queue()
queue.is_empty()
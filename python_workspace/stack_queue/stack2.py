class Stack():

    def __init__(self, max_size, stack):
        self.stack = []
        self.max_size = max_size

    def push(self, element):
        if len(self.stack) > self.max_size:
            print("Size of Stack is Full.")
        else:
            self.stack.append(element)

    def pop(self):
        if len(self.stack) == 0:
            print("Size of stack is zero")
        else:
            self.stack = self.stack[:len(self.stack)-1]

    def top(self):
        print(f"Top element in Queue is {self.stack[-1]}")

    def isFull(self):
        if len(self.stack) == self.max_size:
            print("Size of stack is full..")
    
    def isEmpty(self):
        if len(self.stack) == 0:
            print("Size of stack is Empty..")

    def print_stack(self):
        print(self.stack)

stack = Stack(max_size=3, stack=[])
stack.max_size = 3
stack.isEmpty()
stack.push(10)
stack.push(20)
stack.push(30)
stack.isFull()
stack.pop()
stack.print_stack()
stack.top()
stack.pop()
stack.print_stack()



class Stack():

    def __init__(self, stack = None):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        self.stack = self.stack[:-1]

    def print_stack(self):
        print(self.stack)
        
    def peek(self):
        print("Top Element is : ", self.stack[-1]) 

    def is_empty(self):
        if len(self.stack) == 0:
            print("stack is empty")
        else:
            print("length of stack is ", len(self.stack)) 


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.print_stack()
stack.peek()
stack.pop()
stack.print_stack()
stack.is_empty()
stack.pop() 
stack.print_stack()
stack.pop()
stack.print_stack()
stack.is_empty()
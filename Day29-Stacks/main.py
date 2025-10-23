class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed into stack")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow! Cannot pop.")
            return None
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty!")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Current Stack:", self.stack)



s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()

print("Top element:", s.peek())
print("Popped element:", s.pop())
s.display()
print("Is empty?", s.is_empty())

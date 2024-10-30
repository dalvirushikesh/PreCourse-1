# Time Complexity: O(1) for all the methods as they take constant ti 
# Space Complexity: O(n) where n is the number of elements in the stack

class myStack:
    def __init__(self):
        self.stack = []  

    def isEmpty(self):
        return len(self.stack) == 0  

    def push(self, item):
        self.stack.append(item) 

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop() 
        else:
            return "Stack is empty"

    def peek(self):
        if not self.isEmpty():    
            return self.stack[-1]  
        else:
            return "Stack is empty"

    def size(self):
        return len(self.stack)   

    def show(self):
        return self.stack   # returning the stack


s = myStack()
s.push('6')
s.push('7')
print(s.pop()) 
print(s.show())  

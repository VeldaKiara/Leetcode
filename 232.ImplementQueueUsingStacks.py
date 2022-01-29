'''
when pushing items to the second stack, 
pop the first stack and push it to the second stack

append x to the first stack

in second stack pop the second stack and push it to the first stack

Push: A queue is FIFO (first-in-first-out) but a stack is 
LIFO (last-in-first-out). This means the newest element 
must be pushed to the bottom of the stack. To do so we first
transfer all stack 1 elements to auxiliary stack stack 2. Then the newly
 arrived element is pushed on top of stack 2 and all its elements are 
 popped and pushed to stack 1.
Pop: The algorithm pops an element from the stack 1, 
because stack 1 stores always on its top the first inserted 
element in the queue. The front element of the queue is kept as front.
time and space O(1)
empty:Stack 1 contains all stack elements, 
so the algorithm checks stack 1 size to return if the queue is empty.
Peek

The front element is kept in constant memory and 
is modified when we push or pop an element.

'''
class MyQueue:
    def __init__(self):
        self.firstStack = [ ]
        self.secondStack = [ ]

    def push(self, x) -> None:
        while self.firstStack:
            self.secondStack.append(self.firstStack.pop())
        self.firstStack.append(x)
        while self.secondStack:
            self.firstStack.append(self.secondStack.pop())

    def pop(self):
        return self.firstStack.pop()
        

    def peek(self):
        return self.firstStack[-1]
        
    def empty(self):
        return not self.firstStack
        
'''
push O(1), pop O(1) amortized
push:The newly arrived element is always added on 
top of stack stack 1 and the first element is kept as front queue element
pop:We have to remove element in front of the queue. This is
the first inserted element in the stack stack 1 and it is
positioned at the bottom of the stack because of stack's 
LIFO (last in - first out) policy. To remove the bottom element from stack 1, 
we have to pop all elements from stack 1 and to push them on to an additional 
stack stack 2, which helps us to store the elements of stack 1 in reversed order. 
This way the bottom element of stack 1 will be positioned on top of stack 2 and 
we can simply pop it from stack stack 2. Once stack 2 is empty, the algorithm 
transfer data from stack 1 to stack 2 again.
empty:Both stacks stack 1 and stack 2 contain all stack elements, 
so the algorithm checks stack 1 and stack 2 size to return if the queue is empty.
Peek:The front element is kept in constant memory and 
is modified when we push an element. When stack 2 is not empty,
front element is positioned on the top of stack 2
'''
class MyQueue:
    
    def __init__(self):
        self.firstStack = [ ]
        self.secondStack = [ ]

    def push(self, x) -> None:
        self.firstStack.append(x)
        
    def pop(self):
        self.peek()
        return self.secondStack.pop()
        

    def peek(self):
        if not self.secondStack:
            while self.firstStack:
                self.secondStack.append(self.firstStack.pop())
        return self.secondStack[-1]
        
    def empty(self):
        return not self.firstStack and not self.secondStack
        

        
from Stacks import ArrayStack as Stack 
'''
S = Stack();

S.push(1)
S.push(2)
S.push(3)
S.push(4)

print("The contents of the stack are: ")
S.showElements();
print(S.top() , " is at the top")
print(S.pop(), "Removing the top element.")
print(S.pop(), "Removing the top element.")
print(S.pop(), "Removing the top element.")
print(S.pop(), "Removing the top element.")

print("The contents of the stack are: ")
S.showElements()
print("Is the Stack Empty? ", S.is_empty())
'''

def is_matched(expr):
    '''Return True if all delimiters are properly match; 
    False otherwise.'''
    lefty = '({['
    righty = ')}]'
    S = Stack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()

print(is_matched('({[hello]})'))
print(is_matched('({[hello]}){'))

def reverse_file(filename):
    '''Overwrite given file
    with its contents in reverse order.'''
    S = Stack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n')) #we will re-insert newlines when writing
    original.close()
    #now we overwrite the contents in LIFO order
    original = open(filename, 'w') #reopening file overwrites original
    for i in range(len(S)):
        original.write(S.pop() + '\n') #re-insert newline characterss
    original.close()

reverse_file('myfile.txt')
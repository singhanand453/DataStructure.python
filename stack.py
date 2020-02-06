'''
#basic program for stack push and pop
stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(10)
stack.pop()
print(stack)
'''


from sys import maxsize
def createstack():
    stack=[]
    return stack
def isEmpty(stack):
    return len(stack)==0

def push(stack,item):
    stack.append(item)
    print(item +"pushed")

def pop(stack):
    if (isEmpty(stack)):
        return str(maxsize-1)

    return stack.pop()

def peek(stack):
    if (isEmpty(stack)):
        return str(maxsize-1)
    return stack[len(stack)-1]

stack=createstack()
push(stack,str(20))
push(stack,str(30))
push(stack,str(40))
push(stack,str(10))
print(pop(stack) +"popped")
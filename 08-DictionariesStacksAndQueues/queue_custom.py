#####
# Queue definition
##

stack = []

# add value at the top of the stack
def put(value):
    stack.append(value)
    
# remove the topmost element of the stack
# and return its value    
def get():
    if not empty():
        return stack.pop(0)
    else:
        return None
    
# return true if the stack is empty
def empty():
    return len(stack) == 0

# display stack
def display():
    for i in range(len(stack)):
        print(stack[i])
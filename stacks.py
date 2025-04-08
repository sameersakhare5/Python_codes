stack=[]
def push():
    element = input("enter the element")
    append.stack(element)
    print(stack)
    
def pop():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element".e)
        print(stack)
        
        
while True:
    print ("1.push 2.pop 3.quit")
    choice = int(input())
    if choice==1:
        push()
    elif choice ==2:
        pop()
    elif coice ==3:
        break
#     else:
#         print("enter valid input")

# this is a practice code

# implemented stack using deque to fill the stack rom the other end also we can use quaue LifoQuaue for stack 



import collections 
stack = collections.deque()
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
stack.pop()
print(stack)

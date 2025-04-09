queue.insert(0,10)
queue.insert(0,20)
queue.insert(0,30)
print(queue)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def enque():
  element= int(input("enter the element"))
  queue.append(element)

  print(element)

def deque():
  if not queue:
    print("queue is empty")
  else:
    e=queue.pop(0)
    print("element is been removed",e)
    

def display():
  print(queue)


while True:
  print("select the operation 1.add 2.remove 3.show 4.quit")
  choice=int(input())
  if choice==1:
    enque()
  elif choice ==2:
    deque()
  elif choice ==3:
    display()
  elif choice ==4:
    break
  else:
    print("enter valid input")


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




import collections 
q=collections.deque()
q.append(10)
q.append(20)
q.append(30)
q.append(40)
print(q)

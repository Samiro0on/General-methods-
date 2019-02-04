# name : Samir , @samiro0on , mail: mahmoudsamir109@gmail.com
# Queue and Stack implementation

# 02/03/2019
# FIFO
class Queue:

    def __init__(self):
        self.myQueue = []


    def view(self):
        for item in self.myQueue:
            print(item)                  # or print(self.myQueue)

    def push(self):
        item = input("Please enter the item you want to add to your Queue: ")
        self.myQueue.append(item)

    def pop(self):
        if len(self.myQueue) >= 1:
            self.myQueue.pop(0)          # you can put it in a var if you gonna need it later


q1 = Queue()
# test case 1
while True:
    print("my python implementation of a queue")
    print("*******************************************")
    print("1. view the queue ")
    print("2. add an element")
    print("3. remove an element from queue")
    choice = int(input("please enter your choice 1,2,3: "))
    print("*******************************************")

    if choice == 1:
        q1.view()
    elif choice == 2:
        q1.push()
    elif choice == 3:
        q1.pop()
    else:
        break

# stack FILO
class Stack(Queue):

    def pop(self):
        if len(self.myQueue) >= 1:
            self.myQueue.pop(-1)          # you can put it in a var if you gonna need it later

st = Stack()

#test case 2
while True:
    print("my python implementation of a stack")
    print("*******************************************")
    print("1. view the stack ")
    print("2. add an element")
    print("3. remove an element from stack")
    choice = int(input("please enter your choice 1,2,3: "))
    print("*******************************************")

    if choice == 1:
        st.view()
    elif choice == 2:
        st.push()
    elif choice == 3:
        st.pop()
    else:
        break


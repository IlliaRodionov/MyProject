from random import randint
from time import sleep


class Stack:

    def __init__(self, name=None):
        self.name = name
        self.stack_list = []

    def __repr__(self):
        return f"{self.name} - {self.stack_list}"

    def present(self):
        return f"{self.name} = {self.stack_list}"

    def push(self, value):
        if value < 50:
            print(value)
            sleep(1)
        elif value > 50:
            print(value)
            sleep(2)

    def pop(self):
        pass

class StackAsinc:
    def __init__(self):
        pass

def generator(num):
    for i in range(randint(1, 100)):
        yield i

def main():
   pass



print(generator(10))

stack1 = Stack(name="stack1")
print(stack1)
stack1.push(10)

stack2 = Stack(name="stack2")
print(stack2)

print(generator(10))
# print(main())
if __name__ == "__main__":
    main()




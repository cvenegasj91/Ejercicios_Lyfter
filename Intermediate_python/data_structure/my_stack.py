class Node:
    data: str

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

#LIFO  10 20 30 
class Stack:

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def push(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head:
            self.head = self.head.next


stack = Stack(Node("Soy el primer nodo"))

print("Agregando elementos")

stack.push(Node("Soy el segundo nodo"))
stack.push(Node("Soy el terecer nodo"))

stack.print_structure()

print("quitando elementos")

stack.pop()

stack.print_structure()
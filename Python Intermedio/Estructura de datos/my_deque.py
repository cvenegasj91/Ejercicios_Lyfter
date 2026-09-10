class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Deque:
    def __init__(self, head):
            self.head = head
    
    def print_structure(self):
        current_node = self.head
    
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next
    
    def push_left(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def push_right(self, new_node):
        current_node = self.head
        
        while current_node.next is not None:
            current_node = current_node.next
        
        current_node.next = new_node

    def pop_right(self,):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current_node = self.head

        while current_node.next.next is not None:
            current_node = current_node.next

        current_node.next = None

    def pop_left(self):
            if self.head:
                self.head = self.head.next



deque = Deque(Node("Hola"))
deque.print_structure()

print("Agregando elementos al final")

deque.push_right(Node("Mundo"))
deque.push_right(Node("Soy el primer nodo"))
deque.print_structure()

print("Agregando elementos al inicio")

deque.push_left(Node("Antes de Hola"))
deque.push_left(Node("El antes antes de Hola"))
deque.print_structure()

print("quitando elementos al inicio")

deque.pop_left()
deque.pop_left()
deque.print_structure()

print("Quitando elementos al final")

deque.pop_right()
deque.pop_right()
deque.print_structure()
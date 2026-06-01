from datetime import datetime

class Order:
    def __init__(self, id, customer, details):
        self.id = id
        self.customer = customer
        self.details = details
        self.created_at = datetime.now().strftime("%H:%M:%S")

    def __str__(self):
        return f"{self.id} - {self.customer} - {self.details} - {self.created_at}"
    
class Orderlist:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self, order):
            self.order, self.next = order, None

    def append(self, order):
        new_node = self.Node(order)
        if not self.head:
            self.head = new_node
            return
        
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def display(self):
        cur = self.head
        while cur:
            print(cur.order)
            cur = cur.next

    def reverse(self):
        prev, cur = None, self.head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        self.head = prev

orders = Orderlist()
orders.append(Order(1, "Alice", "laptop"))
orders.append(Order(2, "Bob", "Phone"))
orders.append(Order(3, "John", "Watch"))

print ("Orders in original order:")
orders.display()

orders.reverse()

print("Orders in reversed order:")
orders.display()
"""
It is used when we have to perform an operation on a group of similar kind
of Objects. With the help of visitor pattern, we can move the operational
logic from the objects to another class.

Visitor:
  An abstract class used to declare the visit operations for all the types
  of visitable classes.

ConcreteVisitor:
  For each type of visitor all the visit methods, declared in abstract
  visitor, are implemented in ConcreteVisitor class.

Visitable: An abstract class that is used to declare accept operation.
  The Visitable class provides the access to the object(s) to be “visited”
  by the visitor class object.

ConcreteVisitable: Classes that inherit the Visitable class and
   defines the accept operation. The visitor-object is passed to
   ConcereteVisitable- object(s) using the accept operation.

ObjectStructure: Class that contains all the objects that can be visited.
   ObjectStructure class also has a mechanism to iterate through all the
   objects in the object hierarchy.
"""
from abc import abstractmethod


class Item:
    """Visitable class"""
    @abstractmethod
    def accept(self):
        raise NotImplementedError('Method must be implemented by subclass')


class Visitor:
    """Abstract Vistor Class"""
    @abstractmethod
    def visit(self, item):
        pass


class Shirt(Item):
    def __init__(self, price, size):
        self.price = price
        self.size = size

    def get_price(self):
        return self.price

    def get_size(self):
        return self.size

    def accept(self, visitor):
        return visitor.visit(self)


class Book(Item):
    def __init__(self, cost, genre):
        self.cost = cost
        self.genre = genre

    def get_cost(self):
        return self.cost

    def get_genre(self):
        return self.genre

    def accept(self, visitor):
        return visitor.visit(self)


class CartVisitor(Visitor):
    """serving as ConcereteVisitor and ObjectStructure class."""
    def visit(self, item):
        if isinstance(item, Book):
            cost = item.get_cost()
            print("Book Genre: {}, cost = ${}".format(item.get_genre(), cost))
            return cost
        elif isinstance(item, Shirt):
            cost = item.get_price()
            print("Shirt, size{} cost = ${}".format(item.get_size(), cost))
            return cost


def calculate_price(items):
    visitor = CartVisitor()
    sum = 0
    for item in items:
        sum = sum + item.accept(visitor)

    return sum


if __name__ == '__main__':
    items = [
        Shirt(10, "XL"),
        Shirt(15, "XXL"),
        Book(20, "Fiction"),
        Book(100, "Self Help"),
    ]

    total = calculate_price(items)
    print("Total Cost = ${}".format(total))
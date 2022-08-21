from abc import ABC, abstractmethod


class IVisitor(ABC):

    @abstractmethod
    def visit(self):
        raise NotImplementedError('Method must be implemented by subclass')


class IVisitable(ABC):

    @abstractmethod
    def accept(self):
        raise NotImplementedError('Method must be implemented by subclass')


class Body(IVisitable):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def accept(self, visitor):
        return visitor.visit(self)


class Engine(IVisitable):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def accept(self, visitor):
        return visitor.visit(self)


class Wheel(IVisitable):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def accept(self, visitor):
        return visitor.visit(self)


class Car(IVisitable):

    def __init__(self, name):
        self.name = name
        self._parts = [
            Body("Utility", 1001),
            Engine("V8 engine", 2555),
            Wheel("FrontLeft", 136),
            Wheel("FrontRight", 136),
            Wheel("BackLeft", 152),
            Wheel("BackRight", 152),
        ]

    def accept(self, visitor):
        for part in self._parts:
            part.accept(visitor)
        return visitor.visit(self)


class TotalPriceVisitor(IVisitor):
    total_price = 0

    @classmethod
    def visit(cls, element):
        if hasattr(element, 'price'):
            cls.total_price += element.price
        return cls.total_price


car = Car('pride')
car.accept(TotalPriceVisitor)
print('totla ', TotalPriceVisitor.total_price)



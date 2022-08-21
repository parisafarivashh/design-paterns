"""
Facade is a structural design pattern which provides the simpler interface
to a library or complex set of classes. The word Facade is simply referred to
an outer lying interface of complex patterns that contains several
sub-systems. It is a very important part defined by the Gangs of Four
design patterns. In the simple word,
it defines the higher level interface that any subsystem can use.


It will help us to hide the complexity of the subsystem.

There are several advantages of using facade method;

Facade method helps us to isolate our code from the complexity of a subsystem.
It provides the loose coupling between the client and the subsystems.
It makes the testing process easy since it contains convenient methods for
common testing
"""


class Cook:
    def prepare_dish(self):
        self.cutter = Cutter()
        self.cutter.cutVegetables()

        self.boiler = Boiler()
        self.boiler.boilVegetables()

        self.frier = Frier()
        self.frier.fry()


class Cutter(object):
    def cutVegetables(self):
        print("All vegetables are cut")


class Boiler(object):
    def boilVegetables(self):
        print("All vegetables are boiled")


class Frier(object):
    def fry(self):
        print("All vegetables is mixed and fried.")


if __name__ == "__main__":
    cook = Cook()
    cook.prepare_dish()
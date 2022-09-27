### Creational Design Pattern:

creational design patterns are design patterns that deal with object 
creation mechanisms.
trying to create objects in a manner suitable to the situation.

* Factory Method : ```The factory design pattern is used when we have a 
                     superclass with multiple sub-classes and based on input,
                     we need to return one of the sub-class```
                     
* Abstract Factory Method
* Builder Method
* Prototype Method
* Singleton Method

### Structural Design Patterns:
Structural design pattern is a blueprint of how different objects and
classes are combined together to form a bigger structure for 
achieving multiple goals altogether

* Adapter Method
* Bridge Method
* Composite Method
* Decorator Method
* Facade Method : ```It will help us to hide the complexity of the subsystem.```
* Proxy Method: :``` When you want to add some additional behaviors to an 
                  object of some existing class without changing the client code.```
* FlyWeight Method

### Behavioral Design Pattern:
behavioral design patterns are design patterns that identify 
common communication patterns between objects and realize these patterns. 
By doing so, these patterns increase flexibility in carrying out this communication

* Chain of Responsibility Method
* Command Method
* Iterator Method
* Mediator Method : ```It defines the interface for communication between colleague objects.```      
              ```1- Reduce the number of sub-classes: When you have realized that you have created a lot of unnecessary sub-classes, then it is preferred                to use the Mediator method to avoid these unnecessary sub-classes.```
              ``` 2- Air Traffic Controller: Air traffic controller is a great example of a mediator pattern where the airport control room works as a                  mediator for communication between different flights.```

* Memento Method
* Observer Method: 
         ``` Multi-Dependency: We should use this pattern when multiple objects are dependent on the state of one object as it provides a neat and
         well tested design for the same.```         
         ```Getting Notifications: It is used in social media, RSS feeds, email subscription in which you have the option to follow or subscribe and you          receive latest notification. ```           
         Disadvantages    
         ```1) Random Notifications: All the subscribers present gets notification in the random order.
         2) Risky Implementations: If the pattern is not implemented carefully, there are huge chances that you will end up with large complexity                  code.```

* State Method
* Strategy Method
* Template Method
* Visitor Method :```The purpose of a Visitor pattern is to define a new operation
         without introducing the modifications to an existing object structure.
         So the dilemma is that you need to add methods to the base class,
         but you can’t touch the base class.
         Shopping in a supermarket is another common example to explain how visitor patterns work. The person doing their grocery shopping puts                    everything they want in their shopping cart, which can be considered a set of elements from the object structure. 
         The cashier then acts like a visitor, scanning prices and/or weighing each individual shopping item (i.e., element) to calculate the total                cost.```

### Advantages of using Design Patterns
* Reusability 
* Transparent
* Established Solution 
* Established Communication
* Efficient Development 

### proxy vs facade
The proxy pattern is where one object acts as an interface to another object.
The difference between proxy and facade patterns are that 
we can proxies create interfaces for one object. 
But facades can be interfaces for anything.

### proxy vs decorator
Although Proxy and Decorator patterns have similar structures, 
they differ in intention; while Proxy's prime purpose is to facilitate ease 
of use or controlled access, a Decorator attaches additional responsibilities. 
Both Proxy and Adapter patterns hold a reference to the original object

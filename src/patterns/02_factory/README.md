


                                                                                                                                                                                                                                                    

differnce between example 03 and 04 is just basically Enforcement of Method Implementation
Abstract Base Class (ABC and @abstractmethod):

Enforced Contract: When you use an abstract base class, the abstract methods (decorated with @abstractmethod) must be implemented by any subclass. If a subclass does not implement these methods, Python will raise a TypeError when you try to instantiate the subclass.
Design Intent: This approach explicitly indicates that the base class is meant to be a template, and certain methods must be provided by subclasses. It enforces this at the language level.
Regular Base Class:

No Enforcement: In a regular base class, there's no enforcement mechanism that requires subclasses to implement specific methods. Subclasses can override methods, but they’re not required to. If a subclass forgets to implement a method that’s intended to be overridden, this could lead to runtime errors (e.g., calling a method that doesn’t exist or behaves unexpectedly).
Design Intent: This approach is more flexible, allowing subclasses to inherit behavior from the base class or override methods as needed. It doesn’t explicitly enforce the implementation of any methods.





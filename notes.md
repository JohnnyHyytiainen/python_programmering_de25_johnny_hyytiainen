# OOP recap

- oop is a programming paradigm that organizes software design around objects
(Prior to OOP classes we've used functional approaches)


**DRY - DONT REPEAT YOURSELF**
(oop has been dominating in software development since java)
- OOP -> structure -> modular -> reuse code
- |
- V
- Domain modeling  -> abstraction(this "object" is inside this class) -> hide implementation
- |----------------> group similar behaviours together <-----------------------------------|

# Practically
- We instantiate instances from a class
-  ------------- UML ----------------
-  |                                |
-  |-->     Class = person <---------
  - Attributes= +name:str +age:int +height:float +weight:float
-  |                                              |
-  V ------INSTANTIATE INSTANCES------------------V
p1 = Person(name="jordan", age=77, height=188.3, weight=83) <- an instance of the class
p2 = Person(name="emma", age=83, height=163.5, weight=65) <- another instance of the class
- |                                                                                |
- -------------------------->     Also called OBJECTS        <----------------------

- Methods are similar to "behaviours"

-----------------------------------------

# Inheritance to model the domain and reuse code
- the class Patient can inherit instances from the class Person -> You get all attributes from the person class
- BUT you also get the attributes from the patient class. Patient class inherits the person class attributes.
 - you can also have another class - doctor that inherits the attributes from the person class with the attributes from the doctor
 - class.


**TERMINOLOGY**
- Person class = parent
- patient and doctor class = child
- (patient is a person because it inherits the class from person. Same with doctor) -
    - "is a" relationship         <-------------------------------------------------|

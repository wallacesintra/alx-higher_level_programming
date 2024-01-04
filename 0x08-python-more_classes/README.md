Variables that belong to an object or class are referred to as fields

types of field : instance variables - owned by each individual object/instance of the class
                 class variables - shared - they can be accessed by all instances of that class.

the fields and methods can be referred to as the attributes of that class.

Encapsulation - the bundling of data with the methods that operate on that data.

Information hiding - the principle that some internal information or data is "hidden", so that it can't be accidentally changed. 

Data Abstraction = Data Encapsulation + Data Hiding

Encapsulation is accomplished by:
 getter methods - methods for retrieving or accessing the values of attributes,do not change the values of attributes 
 setter methods -  methods used for changing the values of attributes


_name 	Protected - Protected attributes should not be used outside the class definition, unless inside a subclass definition
__name 	Private   -  This kind of attribute is inaccessible and invisible. It's neither possible to read nor write to those attributes, 
                    except inside the class definition itself.


[InstanceMethods]:

    Regular methods in a class are instance methods.
    They take the instance (self) as the first parameter, and they can access and modify the instance's attributes.
    Use instance methods when you need to access or modify instance-specific data.

class MyClass:
    def instance_method(self, arg):
        # Access instance attributes using self
        self.some_attribute = arg

[ClassMethods] (@classmethod):

    Class methods are bound to the class, not the instance of the class.
    They take the class itself as the first parameter (cls by convention) and can be called on the class or an instance of the class.
    They are often used for factory methods or methods that need to operate on the class itself.
    class methods when the method needs to operate on the class itself or class-level data.

class MyClass:
    class_attribute = "class attribute"

    @classmethod
    def class_method(cls, arg):
        # Access class attributes using cls
        cls.class_attribute = arg


[StaticMethods] (@staticmethod):

    Static methods are not bound to the class or the instance.
    They don't take the class or instance as the first parameter.
    They are independent of the class and can be called on the class or an instance.
    static methods when the method doesn't depend on the instance or class and doesn't need access to their attributes.

class MyClass:
    @staticmethod
    def static_method(arg):
        # No access to instance or class attributes
        pass



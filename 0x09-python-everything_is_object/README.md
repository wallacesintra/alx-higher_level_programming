Everything is object
These things have names — they are called [objects]. An object is something a variable can refer to.
object and values:

a = "banana"
b = "banana"
>>> a == b
True

>>> a is b
True

>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a == b
True
>>> a is b
False
a and b have the same value but do not refer to the same object.
import unittest
from Employee import Employee

class testEmployee(unittest.TestCase):
    def setUp(self):
        self.emp1 = Employee('Wallace', 'Otieno', 270000)
        self.emp_2 = Employee("Otieno", "Benjamin", 310000)

    def tearDown(self):
        pass
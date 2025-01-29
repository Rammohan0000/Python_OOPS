# Assertion is used to check whether a condition is True, and if it is False, the program raises an AssertionError exception.
# Helps in validating assumption during development.
# syntax of assert follows 
assert condition, "Optional error message"
# If the condition is True, the program will continue to execute. If the condition is False, the program will raise an AssertionError exception with the optional error message.
# example
x = 10
assert x > 5, "x should be greater than 5"  
assert x < 5, "x should be less than 5"  

# types of assertions
# 1. Simple assert statement
#example
assert 2 + 2 == 4
assert 2 + 2 == 5 

# 2. AssertEqual()
import unittest
class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 3, 5) 
if __name__ == "__main__":
    unittest.main()

# 3. AssertNotEqual()
import unittest
class TestMath(unittest.TestCase):
    def test_subtraction(self):
        self.assertNotEqual(10 - 5, 3)  
if __name__ == "__main__":
    unittest.main()

# 4. AssertTrue() and AssertFalse()
import unittest
class TestBoolean(unittest.TestCase):
    def test_boolean(self):
        self.assertTrue(3 > 2)  
        self.assertFalse(2 > 3)  
if __name__ == "__main__":
    unittest.main()

# 5. AssertIs() and AssertIsNot()
import unittest
class TestIdentity(unittest.TestCase):
    def test_identity(self):
        a = None
        b = None
        self.assertIs(a, b)  

        x = [1, 2, 3]
        y = [1, 2, 3]
        self.assertIsNot(x, y)  
if __name__ == "__main__":
    unittest.main()

# 6. AssertIn() and AssertNotIn()
import unittest
class TestMembership(unittest.TestCase):
    def test_membership(self):
        fruits = ["apple", "banana", "cherry"]
        self.assertIn("apple", fruits)  
        self.assertNotIn("grape", fruits) 
if __name__ == "__main__":
    unittest.main()

# AssertRaises()
import unittest
def divide(a, b):
    return a / b
class TestException(unittest.TestCase):
    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)  
if __name__ == "__main__":
    unittest.main()


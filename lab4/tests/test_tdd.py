import unittest
from lab4.main import User


class TestUser(unittest.TestCase):
    def test_creation(self):
        user = User("Alice", "alice@example.com", 25)
        self.assertEqual(user.name, "Alice")
        self.assertEqual(user.email, "alice@example.com")
        self.assertEqual(user.age, 25)

    def test_immutable(self):
        user = User("Alice", "alice@example.com")
        with self.assertRaises(AttributeError):
            user.name = "Bob"

if __name__ == "__main__":
    unittest.main()

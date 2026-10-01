import unittest
from app import handler

class TestApp(unittest.TestCase):
    def test_handler_status(self):
        response = handler()
        self.assertEqual(response["statusCode"], 200)

if __name__ == "__main__":
    unittest.main()

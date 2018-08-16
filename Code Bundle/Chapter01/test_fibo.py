import unittest
from fibo import fibonacci


class Test(unittest.TestCase):

    def test_fibo(self):
        result = fibonacci(4)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()

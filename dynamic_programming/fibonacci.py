import unittest

def fib(n):
    l = [0, 1]
    if n > 1:
        for i in range(2, n+1):
            l.append(l[i-1] + l[i-2])

    return l[n]
    

class TestFibonacci(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)

    def test_small_numbers(self):
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(6), 8)
        self.assertEqual(fib(7), 13)

    def test_larger_number(self):
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(15), 610)


if __name__ == "__main__":
    unittest.main()
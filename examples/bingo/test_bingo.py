import unittest

from bingo import Bingo


class TestBingo(unittest.TestCase):
    def test_len(self):
        cage = Bingo([1, 2, 3])
        self.assertTrue(len(cage), 3)

    def test_pop(self):
        cage = Bingo([1])
        self.assertEqual(cage.pop(), 1)
        self.assertEqual(len(cage), 0)

    def test_pop_is_random(self):
        balls = list(range(100))
        cage = Bingo(balls)
        results = []
        while cage:
            results.append(cage.pop())
        self.assertNotEqual(balls, results)
        self.assertNotEqual(balls, list(reversed(results)))


if __name__ == "__main__":
    unittest.main()

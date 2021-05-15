import unittest
from unitTests import circle_area
from math import pi


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # test areas when radius > = 0
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(2.2), pi * 2.2 ** 2)

        # python -m unittest test_unitTests
        # Ran 1 test in 0.001s
        #
        # OK

    def test_values(self):
        # make sure value errors are raised when necessary
        self.assertRaises(ValueError, circle_area, -2)
        # FAILED (failures=1)
        #
        # Failure

        # after checking if r < 0

        # Ran 2 tests in 0.001s
        #
        # OK

    def test_types(self):
        # make sure type errors are raised when necessary
        self.assertRaises(TypeError, circle_area, "string")  # string
        self.assertRaises(TypeError, circle_area, 3 + 5j)  # complex number
        self.assertRaises(TypeError, circle_area, True)  # boolean

        # Ran 1 test in 0.001s
        #
        # OK


help(unittest.TestCase.assertGreaterEqual)
# assertGreaterEqual(self, a, b, msg=None)
#     Just like self.assertTrue(a >= b), but with a nicer default message.

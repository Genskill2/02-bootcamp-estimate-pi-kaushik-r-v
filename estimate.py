import math
import unittest
import random


def wallis(i):
    wallis_pi = 1.0
    for j in range(1,i + 1):
        temp = 4*j*j
        wallis_pi = wallis_pi * (temp/(temp-1))
    return 2*wallis_pi


def monte_carlo(i):
    count_square = 0
    count_circle = 0
    for l in range(i):
        x = (2*random.random()) - 1
        y = (2*random.random()) - 1
        dist = math.sqrt((x*x) + (y*y))
        if dist < 1:
            count_circle = count_circle + 1
        count_square = count_square +1
    pi_value = 4.0*(count_circle/count_square)
    return pi_value


class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()

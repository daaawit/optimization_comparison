import matplotlib.pyplot as plt
import numpy as np


class rosenbrock:
    def __init__(self, x: np.ndarray) -> None:
        self.x = x

    def func(self):
        res = 0
        for i in range(len(self.x)-1):
            res += 100*(self.x[i+1] - self.x[i]) ^ 2 + (1 - self.x[i] ^ 2)
        return res

    def first_derivative(self):
        pass

    def second_derivative(self):
        pass

    def proifle_plot(self):
        pass

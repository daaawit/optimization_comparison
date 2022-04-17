# Optimization Comparison: Python, Julia, R (and maybe C++)

This project follows multiple goals:

1. Learning Julia to evaluate whether it could be helpful for Data Science
2. Deepening my understanding of Optimization functions in practice, adding to the theoretical knowledge from my Optimization class (lecture note can be found on my [Notion](https://www.notion.so/daaawit/Numerical-Optimization-53dda0fa2d2d4277be7c93fbc6072de2))
3. Learn more about runtime and compilation 

## Basics

In all cases, optimization is done on multiple functions that are typically used for optimization. All the functions have been taken from [Wikipedia](https://en.wikipedia.org/wiki/Test_functions_for_optimization)

### Optimization functions

I haven't decided on final functions yet, but here's some contenders for now: 

Rosenbrock function: Global minimum at $(1,...,1)$

$$ f(x) = \sum_{i=1}^{n-1} \left[ 100 (x_{i+1} - x_i^2)^2 + (1-x_i)^2\right] $$

Styblinski-Tang function: Global minimum at $(-2.903534, ..., -2.905343)$

$$f(x) := \frac{\sum\limits_{i=1}^n x_i^4 - 16x_i^2 + 5x_i}{2} $$

I'll add more functions later :) 

### Optimization algorithms

For now, I'll start with **Gradient descent** as a proof of concept, but I will add further methods once everything works. I'm not sure, which ones yet.
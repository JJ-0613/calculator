def power(x,y):
    return x**y

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    """
    Finds a root of a function f using the bisection method.

    Args:
        f (function): The function for which to find the root.
        a (float): The lower bound of the interval.
        b (float): The upper bound of the interval.
        tol (float, optional): The tolerance for the root approximation. Defaults to 1e-6.
        max_iter (int, optional): The maximum number of iterations. Defaults to 100.

    Returns:
        float: The approximated root of the function.

    Raises:
        Exception: If the initial interval [a, b] does not bound a root.
    """

    if f(a) * f(b) >= 0:
        raise Exception("The scalars a and b do not bound a root (f(a) and f(b) must have opposite signs).")

    for i in range(max_iter):
        midpoint = (a + b) / 2

        if abs(f(midpoint)) < tol:  # Check if midpoint is close enough to a root
            return midpoint

        if f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint

    # If max_iter is reached without finding a root within tolerance
    return (a + b) / 2

# Example usage:
def example_function(x):
    return x**3 - x - 2

# Find a root of example_function between 1 and 2
try:
    root = bisection_method(example_function, 1, 2)
    print(f"The approximated root is: {root}")
    print(f"f(root) = {example_function(root)}")
except Exception as e:
    print(f"Error: {e}")

# Another example: Finding a root of sin(x) between 3 and 4 (near pi)
import math

def sin_function(x):
    return math.sin(x)

try:
    root_sin = bisection_method(sin_function, 3, 4, tol=1e-7)
    print(f"The approximated root of sin(x) is: {root_sin}")
    print(f"sin(root_sin) = {sin_function(root_sin)}")
except Exception as e:
    print(f"Error: {e}")
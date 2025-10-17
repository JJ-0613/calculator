def get_sum(x,y):
    return x + y

def get_difference(x,y):
    return x - y

def get_product(x,y):
    return x*y

def get_quotient(x,y):
    if y == 0:
        raise ValueError("Cannot divide by 0")
    return x/y
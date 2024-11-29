def add(a, b):
    """
    Function to add two numbers.
    """
    return a + b

def sub(a, b):
    """
    Function to subtract two numbers.
    """
    if a > b:
        return a - b
    else:
        return "Error: 'a' must be greater than 'b'"
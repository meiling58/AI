# file: math_utils.py

def safe_divide(a: float, b: float) -> float:
    """Divide a by b, raising ValueError on division by zero."""
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b

# click enter will get more suggestions from github copilot

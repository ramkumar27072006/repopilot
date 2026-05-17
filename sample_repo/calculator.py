"""
Calculator module providing basic arithmetic operations.

This module contains functions for addition, subtraction, multiplication,
and division operations. All functions support both integers and floats.
"""


def add(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
    
    Returns:
        The sum of a and b
    
    Examples:
        >>> add(2, 3)
        5
        >>> add(2.5, 3.5)
        6.0
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Subtract the second number from the first.
    
    Args:
        a: Number to subtract from (int or float)
        b: Number to subtract (int or float)
    
    Returns:
        The difference of a and b (a - b)
    
    Examples:
        >>> subtract(10, 5)
        5
        >>> subtract(5.5, 2.5)
        3.0
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers together.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
    
    Returns:
        The product of a and b
    
    Examples:
        >>> multiply(2, 3)
        6
        >>> multiply(2.5, 4)
        10.0
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divide the first number by the second.
    
    Args:
        a: Numerator (int or float)
        b: Denominator (int or float)
    
    Returns:
        The quotient of a divided by b
    
    Raises:
        ValueError: If b is zero (division by zero)
    
    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

"""
Comprehensive test suite for RepoPilot sample_repo calculator module.

This test suite covers:
- Basic functionality tests for all calculator functions
- Edge case tests (large numbers, small numbers, floating point precision)
- Input validation tests (None, strings, booleans, special values)
- Failure handling tests (division by zero, type errors)
- Parametrized tests for efficient testing of multiple scenarios
"""

import pytest
import math
import sys
from sample_repo.calculator import add, subtract, multiply, divide


class TestAddFunction:
    """Test suite for the add() function."""
    
    def test_add_positive_numbers(self):
        """Test addition of two positive integers."""
        assert add(2, 3) == 5
        assert add(100, 200) == 300
        assert add(1, 1) == 2
    
    def test_add_negative_numbers(self):
        """Test addition of negative numbers."""
        assert add(-5, -3) == -8
        assert add(-10, -20) == -30
        assert add(-1, -1) == -2
    
    def test_add_mixed_signs(self):
        """Test addition of positive and negative numbers."""
        assert add(5, -3) == 2
        assert add(-5, 3) == -2
        assert add(10, -10) == 0
    
    def test_add_with_zero(self):
        """Test addition with zero."""
        assert add(0, 0) == 0
        assert add(5, 0) == 5
        assert add(0, 5) == 5
        assert add(-5, 0) == -5
    
    def test_add_floats(self):
        """Test addition of floating point numbers."""
        assert add(2.5, 3.5) == 6.0
        assert add(0.1, 0.2) == pytest.approx(0.3)  # Handle floating point precision
        assert add(-2.5, 1.5) == -1.0
    
    def test_add_large_numbers(self):
        """Test addition with very large numbers."""
        large_num = sys.maxsize
        assert add(large_num, 1) == large_num + 1
        assert add(1e308, 1e308) == 2e308
    
    def test_add_small_numbers(self):
        """Test addition with very small numbers near zero."""
        assert add(1e-10, 1e-10) == pytest.approx(2e-10)
        assert add(1e-100, 1e-100) == pytest.approx(2e-100)
    
    @pytest.mark.parametrize("a,b,expected", [
        (1, 2, 3),
        (0, 0, 0),
        (-1, -1, -2),
        (100, -50, 50),
        (2.5, 2.5, 5.0),
        (-10, 10, 0),
    ])
    def test_add_parametrized(self, a, b, expected):
        """Parametrized test for various addition scenarios."""
        assert add(a, b) == pytest.approx(expected)


class TestSubtractFunction:
    """Test suite for the subtract() function."""
    
    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        assert subtract(5, 3) == 2
        assert subtract(100, 50) == 50
        assert subtract(10, 10) == 0
    
    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        assert subtract(-5, -3) == -2
        assert subtract(-10, -20) == 10
        assert subtract(-1, -1) == 0
    
    def test_subtract_mixed_signs(self):
        """Test subtraction with mixed positive and negative numbers."""
        assert subtract(5, -3) == 8
        assert subtract(-5, 3) == -8
        assert subtract(0, -5) == 5
    
    def test_subtract_with_zero(self):
        """Test subtraction with zero."""
        assert subtract(0, 0) == 0
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5
        assert subtract(-5, 0) == -5
    
    def test_subtract_floats(self):
        """Test subtraction of floating point numbers."""
        assert subtract(5.5, 2.5) == 3.0
        assert subtract(0.3, 0.1) == pytest.approx(0.2)
        assert subtract(-2.5, -1.5) == -1.0
    
    def test_subtract_large_numbers(self):
        """Test subtraction with very large numbers."""
        large_num = sys.maxsize
        assert subtract(large_num, 1) == large_num - 1
        assert subtract(1e308, 1e307) == pytest.approx(9e307, rel=1e-10)
    
    @pytest.mark.parametrize("a,b,expected", [
        (10, 5, 5),
        (0, 0, 0),
        (-5, -5, 0),
        (100, 150, -50),
        (7.5, 2.5, 5.0),
        (-10, 10, -20),
    ])
    def test_subtract_parametrized(self, a, b, expected):
        """Parametrized test for various subtraction scenarios."""
        assert subtract(a, b) == pytest.approx(expected)


class TestMultiplyFunction:
    """Test suite for the multiply() function."""
    
    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        assert multiply(2, 3) == 6
        assert multiply(5, 5) == 25
        assert multiply(10, 10) == 100
    
    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        assert multiply(-2, -3) == 6
        assert multiply(-5, -5) == 25
        assert multiply(-1, -1) == 1
    
    def test_multiply_mixed_signs(self):
        """Test multiplication with mixed signs."""
        assert multiply(5, -3) == -15
        assert multiply(-5, 3) == -15
        assert multiply(-10, 2) == -20
    
    def test_multiply_with_zero(self):
        """Test multiplication with zero."""
        assert multiply(0, 0) == 0
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0
        assert multiply(-5, 0) == 0
        assert multiply(0, -5) == 0
    
    def test_multiply_with_one(self):
        """Test multiplication with one (identity property)."""
        assert multiply(5, 1) == 5
        assert multiply(1, 5) == 5
        assert multiply(-5, 1) == -5
        assert multiply(1, -5) == -5
    
    def test_multiply_floats(self):
        """Test multiplication of floating point numbers."""
        assert multiply(2.5, 2.0) == 5.0
        assert multiply(0.1, 0.2) == pytest.approx(0.02)
        assert multiply(-2.5, 2.0) == -5.0
    
    def test_multiply_large_numbers(self):
        """Test multiplication with large numbers."""
        assert multiply(1e100, 1e100) == 1e200
        assert multiply(1000000, 1000000) == 1000000000000
    
    def test_multiply_small_numbers(self):
        """Test multiplication with very small numbers."""
        assert multiply(1e-10, 1e-10) == pytest.approx(1e-20)
        assert multiply(0.0001, 0.0001) == pytest.approx(1e-8)
    
    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 6),
        (0, 100, 0),
        (-2, -3, 6),
        (-5, 3, -15),
        (2.5, 4, 10.0),
        (1, 999, 999),
    ])
    def test_multiply_parametrized(self, a, b, expected):
        """Parametrized test for various multiplication scenarios."""
        assert multiply(a, b) == pytest.approx(expected)


class TestDivideFunction:
    """Test suite for the divide() function."""
    
    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        assert divide(6, 3) == 2.0
        assert divide(10, 2) == 5.0
        assert divide(100, 10) == 10.0
    
    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        assert divide(-6, -3) == 2.0
        assert divide(-10, -2) == 5.0
        assert divide(-100, -10) == 10.0
    
    def test_divide_mixed_signs(self):
        """Test division with mixed signs."""
        assert divide(6, -3) == -2.0
        assert divide(-6, 3) == -2.0
        assert divide(-10, 2) == -5.0
    
    def test_divide_by_one(self):
        """Test division by one."""
        assert divide(5, 1) == 5.0
        assert divide(-5, 1) == -5.0
        assert divide(0, 1) == 0.0
    
    def test_divide_zero_numerator(self):
        """Test division with zero as numerator."""
        assert divide(0, 5) == 0.0
        assert divide(0, -5) == 0.0
        assert divide(0, 1) == 0.0
    
    def test_divide_floats(self):
        """Test division of floating point numbers."""
        assert divide(5.0, 2.0) == 2.5
        assert divide(7.5, 2.5) == 3.0
        assert divide(1.0, 3.0) == pytest.approx(0.333333, rel=1e-5)
    
    def test_divide_large_numbers(self):
        """Test division with large numbers."""
        assert divide(1e100, 1e50) == 1e50
        assert divide(1000000, 1000) == 1000.0
    
    def test_divide_small_numbers(self):
        """Test division with very small numbers."""
        assert divide(1e-10, 1e-5) == pytest.approx(1e-5)
        assert divide(0.0001, 0.01) == pytest.approx(0.01)
    
    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)
        
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(-5, 0)
        
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(0, 0)
    
    @pytest.mark.parametrize("a,b,expected", [
        (10, 2, 5.0),
        (9, 3, 3.0),
        (-10, 2, -5.0),
        (10, -2, -5.0),
        (7, 2, 3.5),
        (1, 4, 0.25),
    ])
    def test_divide_parametrized(self, a, b, expected):
        """Parametrized test for various division scenarios."""
        assert divide(a, b) == pytest.approx(expected)


class TestInputValidation:
    """Test suite for input validation and type handling."""
    
    def test_add_with_none(self):
        """Test that None values cause TypeError."""
        with pytest.raises(TypeError):
            add(None, 5)
        with pytest.raises(TypeError):
            add(5, None)
        with pytest.raises(TypeError):
            add(None, None)
    
    def test_add_with_strings(self):
        """Test behavior with string inputs (Python concatenates strings)."""
        # Note: Python's + operator concatenates strings, so this actually works
        # but returns unexpected results for a calculator
        result = add("hello", "world")
        assert result == "helloworld"
        
        # Mixing strings and numbers will raise TypeError
        with pytest.raises(TypeError):
            add("5", 5)
    
    def test_add_with_booleans(self):
        """Test behavior with boolean inputs (booleans are treated as 0/1)."""
        # In Python, True == 1 and False == 0
        assert add(True, True) == 2
        assert add(True, False) == 1
        assert add(False, False) == 0
        assert add(5, True) == 6
    
    def test_add_with_lists(self):
        """Test that list inputs cause TypeError or concatenate."""
        # Lists concatenate with +
        result = add([1, 2], [3, 4])
        assert result == [1, 2, 3, 4]
        
        # Mixing list and number raises TypeError
        with pytest.raises(TypeError):
            add([1, 2], 5)
    
    def test_add_with_dicts(self):
        """Test that dict inputs cause TypeError."""
        with pytest.raises(TypeError):
            add({}, {})
        with pytest.raises(TypeError):
            add({"a": 1}, 5)
    
    def test_multiply_with_none(self):
        """Test that None values cause TypeError in multiply."""
        with pytest.raises(TypeError):
            multiply(None, 5)
        with pytest.raises(TypeError):
            multiply(5, None)
    
    def test_divide_with_none(self):
        """Test that None values cause TypeError in divide."""
        with pytest.raises(TypeError):
            divide(None, 5)
        with pytest.raises(TypeError):
            divide(5, None)
    
    def test_subtract_with_strings(self):
        """Test that string inputs cause TypeError in subtract."""
        with pytest.raises(TypeError):
            subtract("10", "5")
        with pytest.raises(TypeError):
            subtract("hello", 5)


class TestSpecialFloatValues:
    """Test suite for special floating point values (inf, -inf, nan)."""
    
    def test_add_with_infinity(self):
        """Test addition with infinity."""
        assert add(float('inf'), 5) == float('inf')
        assert add(5, float('inf')) == float('inf')
        assert add(float('inf'), float('inf')) == float('inf')
        assert add(float('-inf'), 5) == float('-inf')
        # inf + (-inf) is undefined (nan)
        assert math.isnan(add(float('inf'), float('-inf')))
    
    def test_add_with_nan(self):
        """Test addition with NaN (Not a Number)."""
        assert math.isnan(add(float('nan'), 5))
        assert math.isnan(add(5, float('nan')))
        assert math.isnan(add(float('nan'), float('nan')))
    
    def test_multiply_with_infinity(self):
        """Test multiplication with infinity."""
        assert multiply(float('inf'), 5) == float('inf')
        assert multiply(5, float('inf')) == float('inf')
        assert multiply(float('inf'), -5) == float('-inf')
        assert multiply(float('inf'), float('inf')) == float('inf')
        # 0 * inf is undefined (nan)
        assert math.isnan(multiply(0, float('inf')))
    
    def test_multiply_with_nan(self):
        """Test multiplication with NaN."""
        assert math.isnan(multiply(float('nan'), 5))
        assert math.isnan(multiply(5, float('nan')))
    
    def test_divide_with_infinity(self):
        """Test division with infinity."""
        assert divide(float('inf'), 5) == float('inf')
        assert divide(5, float('inf')) == 0.0
        # inf / inf is undefined (nan)
        assert math.isnan(divide(float('inf'), float('inf')))
    
    def test_divide_with_nan(self):
        """Test division with NaN."""
        assert math.isnan(divide(float('nan'), 5))
        assert math.isnan(divide(5, float('nan')))
    
    def test_subtract_with_infinity(self):
        """Test subtraction with infinity."""
        assert subtract(float('inf'), 5) == float('inf')
        assert subtract(5, float('inf')) == float('-inf')
        # inf - inf is undefined (nan)
        assert math.isnan(subtract(float('inf'), float('inf')))


class TestFloatingPointPrecision:
    """Test suite for floating point precision edge cases."""
    
    def test_floating_point_addition_precision(self):
        """Test that floating point addition handles precision correctly."""
        # Classic floating point precision issue
        result = add(0.1, 0.2)
        assert result == pytest.approx(0.3, abs=1e-10)
        
        # Multiple small additions
        result = add(add(0.1, 0.1), 0.1)
        assert result == pytest.approx(0.3, abs=1e-10)
    
    def test_floating_point_subtraction_precision(self):
        """Test floating point subtraction precision."""
        result = subtract(0.3, 0.1)
        assert result == pytest.approx(0.2, abs=1e-10)
        
        result = subtract(1.0, 0.9)
        assert result == pytest.approx(0.1, abs=1e-10)
    
    def test_floating_point_multiplication_precision(self):
        """Test floating point multiplication precision."""
        result = multiply(0.1, 0.1)
        assert result == pytest.approx(0.01, abs=1e-10)
        
        result = multiply(0.3, 3)
        assert result == pytest.approx(0.9, abs=1e-10)
    
    def test_floating_point_division_precision(self):
        """Test floating point division precision."""
        result = divide(1, 3)
        assert result == pytest.approx(0.333333333, rel=1e-9)
        
        result = divide(10, 3)
        assert result == pytest.approx(3.333333333, rel=1e-9)
    
    def test_very_small_number_operations(self):
        """Test operations with very small numbers near machine epsilon."""
        epsilon = sys.float_info.epsilon
        result = add(1.0, epsilon)
        assert result > 1.0
        
        result = subtract(1.0 + epsilon, epsilon)
        assert result == pytest.approx(1.0, abs=1e-15)


class TestMixedIntegerFloatOperations:
    """Test suite for operations mixing integers and floats."""
    
    def test_add_int_and_float(self):
        """Test addition of integers and floats."""
        assert add(5, 2.5) == 7.5
        assert add(2.5, 5) == 7.5
        assert isinstance(add(5, 2.5), float)
    
    def test_subtract_int_and_float(self):
        """Test subtraction of integers and floats."""
        assert subtract(10, 2.5) == 7.5
        assert subtract(2.5, 10) == -7.5
        assert isinstance(subtract(10, 2.5), float)
    
    def test_multiply_int_and_float(self):
        """Test multiplication of integers and floats."""
        assert multiply(5, 2.5) == 12.5
        assert multiply(2.5, 5) == 12.5
        assert isinstance(multiply(5, 2.5), float)
    
    def test_divide_int_and_float(self):
        """Test division of integers and floats."""
        assert divide(10, 2.5) == 4.0
        assert divide(2.5, 10) == 0.25
        # Division always returns float in Python 3
        assert isinstance(divide(10, 2), float)


class TestEdgeCasesAndBoundaries:
    """Test suite for edge cases and boundary conditions."""
    
    def test_maximum_integer_operations(self):
        """Test operations with maximum integer values."""
        max_int = sys.maxsize
        
        # These should work without overflow in Python (arbitrary precision)
        result = add(max_int, 1)
        assert result == max_int + 1
        
        result = multiply(max_int, 2)
        assert result == max_int * 2
    
    def test_minimum_integer_operations(self):
        """Test operations with minimum integer values."""
        min_int = -sys.maxsize - 1
        
        result = subtract(min_int, 1)
        assert result == min_int - 1
        
        result = add(min_int, 1)
        assert result == min_int + 1
    
    def test_operations_near_zero(self):
        """Test operations with numbers very close to zero."""
        tiny = 1e-300
        
        result = add(tiny, tiny)
        assert result == pytest.approx(2 * tiny, rel=1e-10)
        
        result = multiply(tiny, 2)
        assert result == pytest.approx(2 * tiny, rel=1e-10)
    
    def test_divide_resulting_in_very_small_number(self):
        """Test division that results in very small numbers."""
        result = divide(1, 1e100)
        assert result == pytest.approx(1e-100, rel=1e-10)
        
        result = divide(1e-100, 1e100)
        assert result == pytest.approx(1e-200, rel=1e-10)
    
    def test_divide_resulting_in_very_large_number(self):
        """Test division that results in very large numbers."""
        result = divide(1e100, 1e-100)
        assert result == pytest.approx(1e200, rel=1e-10)


# Test fixtures (if needed for future expansion)
@pytest.fixture
def sample_numbers():
    """Fixture providing sample numbers for testing."""
    return {
        'positive': [1, 5, 10, 100],
        'negative': [-1, -5, -10, -100],
        'floats': [1.5, 2.5, 3.14, 0.1],
        'zeros': [0, 0.0, -0.0]
    }


# Additional parametrized tests for comprehensive coverage
@pytest.mark.parametrize("operation,a,b,expected", [
    (add, 1, 1, 2),
    (add, -1, -1, -2),
    (add, 0, 0, 0),
    (subtract, 5, 3, 2),
    (subtract, 3, 5, -2),
    (multiply, 2, 3, 6),
    (multiply, -2, 3, -6),
    (divide, 10, 2, 5.0),
    (divide, -10, 2, -5.0),
])
def test_all_operations_parametrized(operation, a, b, expected):
    """Comprehensive parametrized test for all operations."""
    assert operation(a, b) == pytest.approx(expected)


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v", "--tb=short"])

# Made with Bob

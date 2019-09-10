import pytest

from main import shortestDistance

def test_shortestDistance_returns_float():
    x1 = 5
    y1 = 10
    x2 = 10
    y2 = 10
    
    assert isinstance(shortestDistance.calculate(x1, y1, x2, y2), float)
    
def test_shortestDistance_positive():
    # Shortest distance is 5
    x1 = 5
    y1 = 10
    x2 = 10
    y2 = 10
    
    assert shortestDistance.calculate(x1, y1, x2, y2) == 5.0
    
def test_shortestDistance_negative():
    # Shortest distance is 5
    x1 = -5
    y1 = -10
    x2 = -15
    y2 = -15
    
    assert shortestDistance.calculate(x1, y1, x2, y2) == 11.2
    
def test_shortestDistance_zero():
    # Shortest distance is 5
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    
    assert shortestDistance.calculate(x1, y1, x2, y2) == 0.0
    
def test_shortestDistance_invalid_input_x1():
    with pytest.raises(shortestDistance.InvalidInputError):
        shortestDistance.calculate("x1", 0.0, 0, 0)
    
def test_shortestDistance_invalid_input_y1():
    with pytest.raises(shortestDistance.InvalidInputError):
        shortestDistance.calculate(0, "y1", 0.0, 0)
    
def test_shortestDistance_invalid_input_x2():
    with pytest.raises(shortestDistance.InvalidInputError):
        shortestDistance.calculate(0, 0, "x2", 0.0)
        
def test_shortestDistance_invalid_input_y2():
    with pytest.raises(shortestDistance.InvalidInputError):
        shortestDistance.calculate(0.0, 0, 0, "y2")
import pytest

from main import shortestDistance

def test_shortestDistance_returns_float():  
    assert isinstance(shortestDistance.calculate(10, 10, 10, 10), float)
    
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
        
def test_shortestDistance_floatinput():
    assert shortestDistance.calculate(5.16, 6.32, 9.103455, 7.643) == 4.2
    
def test_shortestDistance_positive():
    assert shortestDistance.calculate(5, 10, 10, 9) == 5.1
    
def test_shortestDistance_negative():
    assert shortestDistance.calculate(-5, -10, -15, -14) == 10.8
    
def test_shortestDistance_zero():
    assert shortestDistance.calculate(0, 0, 0, 0) == 0.0

def test_shortestDistance_roundedToOneDecimalPlace():
    assert (str(shortestDistance.calculate(5, 10, 10, 9))[-2])[0] == "."
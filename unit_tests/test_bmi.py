import pytest

from main import bmi

def test_bmi_returns_tuple():
    assert isinstance(bmi.calculate(5, 10, 150), tuple)
    
def test_bmi_returns_category_string():
    assert isinstance(bmi.calculate(5, 10, 150)[0], str)
    
def test_bmi_returns_bmi_float():
    assert isinstance(bmi.calculate(5, 10, 150)[1], float)
    
def test_bmi_invalid_input_feet():
    with pytest.raises(bmi.InvalidInputError):
        bmi.calculate("feet", 0, 150)
    
def test_bmi_invalid_input_inches():
    with pytest.raises(bmi.InvalidInputError):
        bmi.calculate(5, "inches", 100)
    
def test_bmi_invalid_input_weight():
    with pytest.raises(bmi.InvalidInputError):
        bmi.calculate(5, 5, "weight")
    
def test_bmi_empty_height():
    with pytest.raises(bmi.ZeroHeightError):
        bmi.calculate(0, 0, 150)
    
def test_bmi_empty_weight():
    with pytest.raises(bmi.ZeroWeightError):
        bmi.calculate(5, 1, 0)
    
def test_bmi_formula():
    assert bmi.calculate(5, 5, 90)[1] == 15.3
    
def test_bmi_returns_underweight():
    # BMI is 15.3 - Underweight BMI < 18.5
    assert bmi.calculate(5, 5, 90)[0] == "Underweight"

def test_bmi_returns_normalweight_edge():
    # BMI is 18.5 - Normal weight BMI 18.5-24.9
    assert bmi.calculate(5, 2, 99)[0] == "Normal weight"
    
def test_bmi_returns_normalweight():
    # BMI is 22.7 - Normal weight BMI 18.5-24.9
    assert bmi.calculate(5, 3, 125)[0] == "Normal weight"
    
def test_bmi_returns_overweight_edge():
    # BMI is 25 - Overweight BMI 25-29.9
    assert bmi.calculate(5, 0, 125)[0] == "Overweight"
    
def test_bmi_returns_overweight():
    # BMI is 27.9 - Overweight BMI 25-29.9 
    assert bmi.calculate(5, 10, 190)[0] == "Overweight"
    
def test_bmi_returns_obese_edge():
    # BMI is 30 - Obese BMI of 30 or greater
    assert bmi.calculate(5, 0, 150)[0] == "Obese"
    
def test_bmi_returns_obese():
    # BMI is 40.0 - Obese BMI of 30 or greater
    assert bmi.calculate(5, 0, 200)[0] == "Obese"
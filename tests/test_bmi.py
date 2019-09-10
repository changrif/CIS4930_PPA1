import pytest

from main import bmi

def test_bmi_returns_tuple():
    feet = 5
    inches = 10
    weight = 150
    
    assert isinstance(bmi.calculate(feet, inches, weight), tuple)
    
def test_bmi_returns_category_string():
    feet = 5
    inches = 10
    weight = 150
    
    assert isinstance(bmi.calculate(feet, inches, weight)[0], str)
    
def test_bmi_returns_bmi_float():
    feet = 5
    inches = 10
    weight = 150
    
    assert isinstance(bmi.calculate(feet, inches, weight)[1], float)
    
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
    feet = 5
    inches = 5
    weight = 90
    
    assert bmi.calculate(feet, inches, weight)[1] == 15.3
    
def test_bmi_returns_underweight():
    # BMI is 15.3 - Underweight BMI < 18.5
    feet = 5
    inches = 5
    weight = 90
    
    assert bmi.calculate(feet, inches, weight)[0] == "Underweight"

def test_bmi_returns_normalweight_edge():
    # BMI is 18.5 - Normal weight BMI 18.5-24.9
    feet = 5
    inches = 2
    weight = 99
    
    assert bmi.calculate(feet, inches, weight)[0] == "Normal weight"
    
def test_bmi_returns_normalweight():
    # BMI is 22.7 - Normal weight BMI 18.5-24.9
    feet = 5
    inches = 3
    weight = 125
    
    assert bmi.calculate(feet, inches, weight)[0] == "Normal weight"
    
def test_bmi_returns_overweight_edge():
    # BMI is 25 - Overweight BMI 25-29.9
    feet = 5
    inches = 0
    weight = 125
    
    assert bmi.calculate(feet, inches, weight)[0] == "Overweight"
    
def test_bmi_returns_overweight():
    # BMI is 27.9 - Overweight BMI 25-29.9
    feet = 5
    inches = 10
    weight = 190
    
    assert bmi.calculate(feet, inches, weight)[0] == "Overweight"
    
def test_bmi_returns_obese_edge():
    # BMI is 30 - Obese BMI of 30 or greater
    feet = 5
    inches = 0
    weight = 150
    
    assert bmi.calculate(feet, inches, weight)[0] == "Obese"
    
def test_bmi_returns_obese():
    # BMI is 40.0 - Obese BMI of 30 or greater
    feet = 5
    inches = 0
    weight = 200
    
    assert bmi.calculate(feet, inches, weight)[0] == "Obese"
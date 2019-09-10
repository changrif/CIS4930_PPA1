import pytest

from main import tip

def test_tip_returns_float():
    assert isinstance(tip.calculate(20, 3), tuple)
    
def test_tip_total_invalid_input():
    with pytest.raises(tip.InvalidInputError):
        tip.calculate("test", 3)
    
def test_tip_guests_invalid_input():
    with pytest.raises(tip.InvalidInputError):
        tip.calculate(20.3, "test")
        
def test_tip_total_zero():
    with pytest.raises(tip.InvalidTotalError):
        tip.calculate(0, 3)
    
def test_tip_guests_zero():
    with pytest.raises(tip.InvalidGuestsError):
        tip.calculate(20.3, 0)
        
def test_tip_total_negative():
    with pytest.raises(tip.InvalidTotalError):
        tip.calculate(-1, 3)
    
def test_tip_guests_negative():
    with pytest.raises(tip.InvalidGuestsError):
        tip.calculate(20.3, -1)
        
def test_tip_gratuity():
    # 15% gratuity
    assert tip.calculate(20, 1)[0] == 23
    
def test_tip_split_twoCentsMore():
    assert tip.calculate(15.17, 3)[1] == [5.82, 5.82, 5.81]
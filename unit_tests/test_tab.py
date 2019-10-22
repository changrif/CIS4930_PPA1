import pytest

from main import tab

def test_tab_returns_float():
    assert isinstance(tab.calculate(20, 3), tuple)
    
def test_tab_total_returns_string():
    assert isinstance(tab.calculate(20, 3)[0], str)
    
def test_tab_split_returns_list():
    assert isinstance(tab.calculate(20, 3)[1], list)
    
def test_tab_split_list_returns_string():
    assert isinstance(tab.calculate(20, 3)[1][0], str)
    
def test_tab_total_roundedToTwoDecimalPlaces():
    assert (str(tab.calculate(115, 1)[0])[-3])[0] == "."
    
def test_tab_split_roundedToTwoDecimalPlaces():
    assert (str(tab.calculate(115, 1)[1][0])[-3])[0] == "."
    
def test_tab_total_invalid_input():
    with pytest.raises(tab.InvalidInputError):
        tab.calculate("test", 3)
    
def test_tab_guests_invalid_input():
    with pytest.raises(tab.InvalidInputError):
        tab.calculate(20.3, "test")
        
def test_tab_total_zero():
    with pytest.raises(tab.InvalidTotalError):
        tab.calculate(0, 3)
    
def test_tab_guests_zero():
    with pytest.raises(tab.InvalidGuestsError):
        tab.calculate(20.3, 0)
        
def test_tab_total_negative():
    with pytest.raises(tab.InvalidTotalError):
        tab.calculate(-1, 3)
    
def test_tab_guests_negative():
    with pytest.raises(tab.InvalidGuestsError):
        tab.calculate(20.3, -1)
        
def test_tab_total_addgratuity():
    # 15% gratuity
    assert tab.calculate(20, 1)[0] == '23.00'
    
def test_tab_split_even():
    assert tab.calculate(20, 2)[1] == ['11.50', '11.50']
    
def test_tab_split_unevenByOne():
    assert tab.calculate(2.01, 2)[1] == ['1.16', '1.15']
    
def test_tab_split_unevenByTwo():
    assert tab.calculate(15.17, 3)[1] == ['5.82', '5.82', '5.81']
    
def test_tab_split_once():
    assert tab.calculate(8, 1)[1] == ['9.20']
    
def test_tab_split_twice():
    assert tab.calculate(8, 2)[1] == ['4.60', '4.60']
    
def test_tab_split_thrice():
    assert tab.calculate(8, 3)[1] == ['3.07', '3.07', '3.06']
    
def test_tab_split_four():
    assert tab.calculate(8, 4)[1] == ['2.30', '2.30', '2.30', '2.30']
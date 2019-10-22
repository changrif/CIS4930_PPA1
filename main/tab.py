import math

class InvalidInputError(Exception):
   """Raised when the input value is not a number"""
   pass

class InvalidTotalError(Exception):
   """Raised when the total check input value is not numeric, greater than zero"""
   pass

class InvalidGuestsError(Exception):
   """Raised when the guests input value is not an integer greater than zero"""
   pass

# *****************************************************************************************
# *** CALCULATE METHOD - Takes in total and guests, returns total and splits per person ***
# *****************************************************************************************
def calculate(total, numGuests):
    try:
        total = float(total)
        numGuests = int(numGuests)
    except Exception:
        raise InvalidInputError
    
    if total <= 0:
        raise InvalidTotalError
    if numGuests <= 0:
        raise InvalidGuestsError
        
    total *= 1.15
    total = round(total, 2)
    split = math.floor((total*100) / numGuests) / 100
    
    splitCheck = ["%.2f" % split] * numGuests
    remainder = round((total % split) * 100, 0)
    i = 0
    while remainder > 0:
        splitCheck[i] = "%.2f" % round(float(splitCheck[i]) + 0.01, 2)
        i += 1
        remainder -= 1
        
    return "%.2f" % total, splitCheck
import math

class InvalidInputError(Exception):
   """Raised when the input value is not an integer or float"""
   pass

# **********************      
# *** CONSOLE METHOD ***
# **********************
def console():
    x1 = raw_input(" x1: ")
    y1 = raw_input(" y1: ")
    x2 = raw_input(" x2: ")
    y2 = raw_input(" y2: ")

    try:
        shortestDistanceNum = calculate(x1, y1, x2, y2)
        print("\n The shortest distance between (" + x1 + ", " + y1 + ") and (" + x2 + ", " + y2 + ") is " + str(shortestDistanceNum) + "\n")
    except Exception as e:
        print("\n Try again: " + type(e).__name__ + "\n")

# *****************************************************************
# *** CALCULATE METHOD - Takes in coordinates, returns distance ***
# *****************************************************************
def calculate(x1, y1, x2, y2):
    try:
        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
    except Exception:
        raise InvalidInputError
    
    xDiffSq = (x2 - x1) * (x2 - x1)
    yDiffSq = (y2 - y1) * (y2 - y1)
    
    return round(math.sqrt(xDiffSq + yDiffSq), 1)
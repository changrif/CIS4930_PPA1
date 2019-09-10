import math

class InvalidInputError(Exception):
   """Raised when the input value is not an integer or float"""
   pass

def calculate(x1, y1, x2, y2):
    try:
        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
    except Exception:
        raise InvalidInputError
    
    xDiffSq = (x2 - x1) * (x2 - x1);
    yDiffSq = (y2 - y1) * (y2 - y1);
    
    return round(math.sqrt(xDiffSq + yDiffSq), 1);
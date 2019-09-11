class InvalidInputError(Exception):
   """Raised when the input value is not an integer"""
   pass

class ZeroWeightError(Exception):
   """Raised when the weight input value is less than or equal to zero pounds"""
   pass

class ZeroHeightError(Exception):
   """Raised when the height input value is less than or equal to zero inches"""
   pass

def calculate(feet, inches, weight):
    try:
        feet = int(feet)
        inches = int(inches)
        weight = int(weight)
    except Exception:
        raise InvalidInputError
    
    if weight <= 0:
        raise ZeroWeightError
    
    if feet < 0 or inches < 0 or (feet == 0 and inches == 0):
        raise ZeroHeightError
    
    weightInKg = weight * 0.45
    heightInM = ((feet * 12) + inches) * 0.025
    bmi = round((weightInKg) / (heightInM * heightInM), 1)
    
    if bmi < 18.5:
        return "Underweight", bmi
    elif bmi < 25:
        return "Normal weight", bmi
    elif bmi < 30:
        return "Overweight", bmi
    
    return "Obese", bmi
import db

class InvalidInputError(Exception):
   """Raised when the input value is not an integer"""
   pass

class ZeroWeightError(Exception):
   """Raised when the weight input value is less than or equal to zero pounds"""
   pass

class ZeroHeightError(Exception):
   """Raised when the height input value is less than or equal to zero inches"""
   pass

# **********************      
# *** CONSOLE METHOD ***
# **********************
def console():
    db.printAllBMI()

    feet = raw_input(" Height (ft): ")
    inches = raw_input(" Height (in): ")
    weight = raw_input(" Weight (lb): ")

    try:
        category, bmiNum = calculate(feet, inches, weight)
        print("\n Your BMI of : " + str(bmiNum) + " is considered " + category + "\n")

        db.saveBMI(feet, inches, weight, category, bmiNum)
    except Exception as e:
        print("\n Try again: " + type(e).__name__ + "\n")

# ****************************************************************************************
# *** CALCULATE METHOD - Takes in feet, inches and weight, returns bmiNum and category ***
# ****************************************************************************************
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
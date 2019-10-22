from main import bmi, shortestDistance, email, tab, db

def run():
    choice = -1
    
    while(choice != "5"):
        choice = raw_input(
              "**********************"
              "\nFunction Menu: "
              "\n (1) Body Mass Index"
              "\n (2) Shortest Distance"
              "\n (3) Email Verifier"
              "\n (4) Split the Tab"
              "\n (5) Quit"
              "\n**********************"
              "\n Choose a Function: ");

        if choice == "1":
            bmi_console();
        elif choice == "2":
            shortestDistance_console();
        elif choice == "3":
            email_console();
        elif choice == "4":
            tab_console();
        elif choice != "5":
            print("\n Not a valid choice. Please enter an integer choice 1-5.\n")

# **********************      
# ***   BMI METHOD   ***
# **********************
def bmi_console():
    db.printAllBMI()

    feet = raw_input(" Height (ft): ")
    inches = raw_input(" Height (in): ")
    weight = raw_input(" Weight (lb): ")

    try:
        category, bmiNum = bmi.calculate(feet, inches, weight)
        print("\n Your BMI of : " + str(bmiNum) + " is considered " + category + "\n")

        db.saveBMI(feet, inches, weight, category, bmiNum)
    except Exception as e:
        print("\n Try again: " + type(e).__name__ + "\n")

# **********************      
# *** DISTANCE METHOD **
# **********************
def shortestDistance_console():
    x1 = raw_input(" x1: ")
    y1 = raw_input(" y1: ")
    x2 = raw_input(" x2: ")
    y2 = raw_input(" y2: ")

    try:
        shortestDistanceNum = shortestDistance.calculate(x1, y1, x2, y2)
        print("\n The shortest distance between (" + x1 + ", " + y1 + ") and (" + x2 + ", " + y2 + ") is " + str(shortestDistanceNum) + "\n")
    except Exception as e:
        print("\n Try again: " + type(e).__name__ + "\n")
        
# **********************      
# ***  EMAIL METHOD  ***
# **********************
def email_console():
    db.printAllEmails();
    address = raw_input(" Email: ")

    try:
        verified = email.verify(address)
        if verified:
            print("\n \"" + address + "\" is a valid email address.\n")
        else:
            print("\n \"" + address + "\" is not a valid email address.\n")

        db.saveEmail(address, verified)
    except Exception as e:
        print("\n Try again: " + type(e).__name__ + "\n")
        
# **********************      
# ***   TAB METHOD   ***
# **********************
def tab_console():
    total = raw_input(" Total: ")
    guests = raw_input(" Guests: ")

    try:
        totalCheck, splitAmount = tab.calculate(total, guests)
        print("\n Total: " + str(totalCheck) + "\n Split Between " + guests + " Guests:" + str(splitAmount) + "\n")
    except Exception as e:
        print("\n Try again: " + type(e).__name__ + "\n")
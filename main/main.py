import bmi, shortestDistance, email, tip

if __name__ == "__main__":
    choice = -1
    
    while(choice != "5"):
        choice = input("**********************"
              "\nFunction Menu: "
              "\n (1) Body Mass Index"
              "\n (2) Shortest Distance"
              "\n (3) Email Verifier"
              "\n (4) Split the Tip"
              "\n (5) Quit"
              "\n**********************"
              "\n Choose a Function: ");

        if choice == "1":
            feet = input(" Height (ft): ")
            inches = input(" Height (in): ")
            weight = input(" Weight (lb): ")

            try:
                category, bmiNum = bmi.calculate(feet, inches, weight)
                print("\n Your BMI of : " + str(bmiNum) + " is considered " + category)
            except Exception as e:
                print("\n Try again: " + type(e).__name__)
        elif choice == "2":
            x1 = input(" x1: ")
            y1 = input(" y1: ")
            x2 = input(" x2: ")
            y2 = input(" y2: ")
            
            try:
                shortestDistanceNum = shortestDistance.calculate(x1, y1, x2, y2)
                print(shortestDistanceNum)
            except Exception as e:
                print(e)
        elif choice == "3":
            address = input(" Email: ")
            
            try:
                print(address)
                verified = email.verify(address)
                print(verified)
            except Exception as e:
                print(e)
        elif choice == "4":
            total = input(" Total: ")
            guests = input(" Guests: ")
            
            try:
                splitAmount = tip.calculate(total, guests)
                print(splitAmount)
            except Exception as e:
                print(e)
        elif choice != "5":
            print("\n Not a valid choice. Please enter an integer choice 1-5.\n")    
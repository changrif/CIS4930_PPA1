from main import bmi, shortestDistance, email, tab

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
            bmi.console();
        elif choice == "2":
            shortestDistance.console();
        elif choice == "3":
            email.console();
        elif choice == "4":
            tab.console();
        elif choice != "5":
            print("\n Not a valid choice. Please enter an integer choice 1-5.\n")
name = str(input("Enter the number of houses: "))

match name:
    case "denish" | "harsh" | "sahil":
        print("Welcome to the house!")
    case _:
        print("Sorry, you are not allowed in the house.")
        
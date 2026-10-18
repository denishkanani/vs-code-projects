def main():
    x = get_integer()
    print(f"x is {x}")

def get_integer():

    while True:
        try:
            x = int(input("what is the value of x? "))
            print(f"the value of x is {x}")
            break
        except ValueError:
            print("x is not an integer")
    return x
    
main()
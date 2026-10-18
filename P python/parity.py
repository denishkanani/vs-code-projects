def main():
    x = int(input("enter a value of x "))
    
    if is_even(x):
        print("even number")
        
    else:
        print("odd number")
        
def is_even(n):
    return n % 2 == 0
    
main()
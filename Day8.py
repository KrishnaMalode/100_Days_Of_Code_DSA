
import cmath  # Use cmath to handle complex numbers instead of using math

def find_roots(a, b, c):
    # Calculate the discriminant
    D = b**2 - 4*a*c
    
    # Calculate the two roots using cmath.sqrt for complex support
    root1 = (-b + cmath.sqrt(D)) / (2 * a)
    root2 = (-b - cmath.sqrt(D)) / (2 * a)
    
    # Print the roots
    print(f'Roots of the equation are {root1} & {root2}')

def main():
    # Input with validation
    while True:
        try:
            a, b, c = map(float, input("Enter three coefficients (a, b, c) separated by spaces: ").split())
            if a == 0:
                print("Coefficient 'a' cannot be zero. Please enter again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter three numerical values.")

    find_roots(a, b, c)

if __name__ == "__main__":
    main()
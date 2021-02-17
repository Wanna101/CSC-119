"""
David Young
CSC119-479
6/6/2020
Fahrenheit to Celsus conversion program
Given fahrenheit convert to celsius
Sample 1: 212 fahrenheit is 100 celsius
Sample 2: 32  fahrenheit is 0   celsius
Sample 3: -5  fahrenheit is -20.56 celsius
"""

def main():  # definition of main program

    fahrenheit = 0.0 # variable - input
    celsius = 0.0    # variable - output

    # input - fahrenheit - come in as a string input() '212'
    fahrenheit = input("Enter FAHRENHEIT: ")
    
    # convert the input to number -float or int         212
    fahrenheit = float(fahrenheit)
    
    # process: celsius = 5/9 ( fahrenheit -32)
    celsius = 5/9 * (fahrenheit - 32)
    
    # output - celsius - print
    print("CELSIUS: ", celsius)

main()      # execution of main program

# fraction-project

This project is a command-line interface calculator that performs arithmetic operations on fractions. It allows users to enter simple arithmetic expressions containing fractions, such as "1/2 + 3/4" or "2 * 1/3", and returns the result as a fraction. The calculator can handle addition, subtraction, multiplication, and division of fractions, as well as whole numbers.

The calculator uses the Fraction class to represent fractions and performs operations on them using methods such as add, sub, mul, and truediv. The class also includes methods to convert strings to fractions and to check for equality between fractions. The calculate function takes a string input, parses it into left and right operands and an operator, converts them to fractions, and applies the corresponding operation to return the result as a fraction. If there is an error in the input format or an unsupported operator, the function returns "BLAD".

The main function provides a simple user interface by repeatedly prompting the user to enter an arithmetic expression and printing the result until the user terminates the program with EOFError (i.e., by pressing Ctrl+D).

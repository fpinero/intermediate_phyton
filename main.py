# this function takes
# one argument, num and
# returns num squared
def square(num):
    numSquared = num * num
    return numSquared


def main():
    print('This line is printed directly from the main function of the program')
    secondary_function()
    # several test cases
    # to verify the function
    # is working as expected

    print(square(2))  # Prints 4
    print(square(5))  # Prints 25
    print(square(8))  # Prints 64
    print(square(10))  # Prints 100


def secondary_function():
    print('This line is printed from a secondary function call within the main function')


if __name__ == '__main__':
    main()

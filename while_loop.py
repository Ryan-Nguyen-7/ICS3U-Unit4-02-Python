# Created by Ryan Nguyen
# Created on December 2020
# This program calculates a factorial of user inpoutted integer


def main():
    # This function calculates factorials

    # loop counter starts at 0
    loop_counter = 1
    # input
    integer_as_string = input("Enter positive integer: ")
    print("")

    # process + output
    try:
        integer_as_number = int(integer_as_string)
        factorial_sum = integer_as_number
        if integer_as_number > 0:
            while loop_counter < integer_as_number:
                factorial_sum = factorial_sum*loop_counter
                loop_counter = loop_counter + 1
            print("{}".format(factorial_sum))
        else:
            print("Integer must be positive")
    except Exception:
        print("Invalid integer")


if __name__ == "__main__":
    main()

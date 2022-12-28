calculation_to_units = 24
name_of_unit = 'hours'


# Define functions
def days_to_units(number_of_days):
    return f"{number_of_days:,} days are equal to {number_of_days * calculation_to_units:,} {name_of_unit}."


def validate_and_execute():
    # Use the isdigit() so that your program will not crash when user input a blank.
    # Handle error with try
    try:
        # if user_input.isdigit():
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You have entered 0 which is invalid! Please try again.")
        else:
            print("You have entered a NEGATIVE number! Please try again.")
    except ValueError:
        print("Try again. You have typed an invalid number. Use positive valid number please. Ex. '10'")


user_input = ''  # This line is used so that the line of While will be read by interpreter and moves to the next line.
while user_input != 'exit':
    user_input = input("\nEnter number of days and conversion unit: ")
    list_of_days = user_input.split(', ')
    print(list_of_days)
    print(type(list_of_days))
    print(set(list_of_days))
    print(type(set(list_of_days)))
    for num_of_days_element in set(list_of_days):
        validate_and_execute()

"""main.py (most updated December 18, 2022)

user_input = ''  # This line is used so that the line of While will be read by interpreter and moves to the next line.
while user_input != 'exit':
    user_input = input(user_input_message)
    days_and_units = user_input.split(':')
    print(days_and_units)
    days_and_unit_dictionary = {'days': days_and_units[0], 'unit': days_and_units[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute(days_and_unit_dictionary)


----------------- helper.py


# Define functions
def days_to_units(number_of_days, conversion_unit):
    if conversion_unit == 'hours':
        return f"{number_of_days:,} days are equal to {number_of_days * 24:,} hours."
    elif conversion_unit == 'minutes':
        return f"{number_of_days:,} days are equal to {number_of_days * 24 * 60:,} minutes."
    else:
        return "Please choose between hours or minutes only."


def validate_and_execute(days_and_unit_dictionary):
    # Use the isdigit() so that your program will not crash when user input a blank.
    # Handle error with try
    try:
        user_input_number = int(days_and_unit_dictionary['days'])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary['unit'])
            print(calculated_value)
        elif user_input_number == 0:
            print("You have entered 0 which is invalid! Please try again.")
        else:
            print("You have entered a NEGATIVE number! Please try again.")
    except ValueError:
        print("Try again. You have typed an invalid number. Use positive valid number please. Ex. '10'")


user_input_message = "\nEnter number of days and conversion unit: "

"""
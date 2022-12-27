"""
time_till_deadline
    a. Accept user input of goal and deadline
    b. Print back:
        how much time remains until that deadline

This is a countdown app

"""

from _datetime import datetime

# Input format: task:mm.dd.yyyy
user_input = input("Enter your goal with deadline, separate it with colon: ")
input_list = user_input.split(":")

goal = input_list[0]  # 1st value
deadline = input_list[1]  # 2nd value

# Converts to date format. For parameters check its document
deadline_date = datetime.strptime(deadline, "%m.%d.%Y")
today_date = datetime.today()

# Calculate days now till deadline
time_till = deadline_date - today_date

# Calculate the remaining hours and remove the float by using int casting.
hours_till = int(time_till.total_seconds() /60 /60)

#  time_till.days will only show the date not the hours.
print(f"Dear user the time remaining for your goal to {goal} is {time_till.days}")

# Calculate the remaining hours
print(f"Dear user the time remaining for your goal to {goal} is {time_till.total_seconds() /60 /60} hours")

# Calculate the remaining hours and remove the float by using int casting.
print(f"Dear user the time remaining for your goal to {goal} is {hours_till}")
"""
age_calculator.py - calculates your age. calculate if you are older than I.
                  - you can calculate age of famous personalities in history.
                  - it will execute until you stop it. Because of while loop.
                  - if the person you want to check lives in time of BC or Before Christ make the year negative
                            example: 600 BC => -600 BC


"""


# Condition for every stage of life
def my_comment():
    if age < -1:
        return 'You are not yet born in this world.'
    elif age < 1:
        return 'You must still be inside your mom\'s womb.'
    elif age < 10:
        return 'So you\'re still in elementary, enjoy your childhood and keep playing!'
    elif age < 20:
        return 'So you\'re in college? Focus on the future ahead of you! Go all out!'
    elif age < 25:
        return 'Time goes by quickly. Go travel!'
    elif age < 30:
        return 'Keep hustling! Never stop learning!'
    elif age < 50:
        return 'Are you near retirement? Don\'t overdo it.'
    elif age < 70:
        return 'You should relax and retire.'
    elif age < 80:
        return 'Did you know that you are born within the time of World War II?'
    elif age < 90:
        return 'Did you know that you are born after World War II? You must have a hard time.'
    elif age < 135:
        return 'You might have known Adolf Hitler of Germany?'
    elif age < 250:
        return 'You might have known Charles Darwin, the mind behind influential theory of evolution?'
    elif age < 500:
        return 'You might have known Galileo Galilei, the father of modern science?'
    elif age < 600:
        return 'You might have known Leonardo da Vinci of the Italian Renaissance?'
    elif age < 700:
        return 'Wow! You got a legendary record! What\'s your secret?'
    elif age < 1000:
        return 'You might have known Genghis Khan, the warrior who founded the first Mongol Empire?'
    elif age < 2000:
        return 'This is majestic! You\'re a mythical legend!'
    elif age < 2170:
        return 'You might have known Julius Caesar of the Roman Empire?'
    elif age < 2380:
        return 'You might have known Alexander the Great of Macedonia?'
    elif age < 2450:
        return 'You might have known Plato the influential philosopher?'
    else:
        return 'I can\'t believe it! Are you immortal?'


# Calculate difference between my age and other people
def age_range():
    if age < 26:
        x = 26 - age
        return x
    elif age >= 26:
        x = age - 26
        return x


# Check if they are younger, older, or the same age
def age_level():
    if age < 26:
        return 'younger than me.'
    elif age > 26:
        return 'older than me.'
    elif age == 26:
        return 'the same with me.'


# Define variables
while True:
    name = input('\n\nPlease enter your name: ')
    birth_month = input('Please enter your birth month: ')
    birth_year = int(input('Please enter your birth year: '))

    # The current year is 2022
    age = 2022 - birth_year
    decades = float(age / 10)
    comment_value = my_comment()
    age_comparison = age_range()
    age_category = age_level()

    print(f"\nHi {name.strip()}! \nSo you're born on {birth_month.strip()} year {birth_year}. "
          f"On my calculation you are now {age:,} years old. {comment_value}")

    print(f"You are living in {decades} decades now "
          f"and you are {age_comparison:,} years {age_category} Amazing!")

"""
A little assignment to practice receiving text input from the user in Python programming.
Do not run this file... run main.py instead.
"""


def get_favorite_vegetable():
    """
    Asks the user to enter their favorite vegetable
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite vegetable.
    """
    # write your code here.
    favorite_vege = input("what is your favorite vegetable?\n")
    start_vege = "Interesting! I also Love "
    end_vege = "!"
    print( start_vege + favorite_vege + end_vege)




def get_favorite_number():
    """
    Asks the user to enter their favorite number
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite number.
    """
    # write your code here.
    ask_favo_numb = input("what is your favorite number?\n")
    start_numb = "Interesting! I also Love "
    end_numb = "!"
    print( start_numb + ask_favo_numb + end_numb)



def get_name_and_zodiac_sign():
    """
    Asks the user to enter their name.
    Then ask them to enter their zodiac sign.
    Then print out, "Interesting! My name is also X, and I'm also a Y!",
    where X and Y are replaced by the user's name and zodiac sign, respectively.
    """
    # write your code here.
    ask_name = input("What is your name?\n")
    ask_zsign = input("What is your zodiac sign?\n")
    start_name = "Interesting! My name is also "
    mid_comma = ", "
    start_zsign = "and I'm also a "
    end_name = "!"
    print( start_name + ask_name + mid_comma + start_zsign + ask_zsign + end_name)




def get_name_and_age():
    """
    Asks the user to enter their name.
    Then ask them to enter their age.
    Then print out, "Interesting! My name is also X, and I'm also Y years old!",
    where X and Y are replaced by the user's name and age, respectively.
    """
    # write your code here.
    ask_name = input("What is your name?\n")
    ask_age = input("How old are you?\n")
    start_name = "Interesting! My name is also "
    mid_comma = ", "
    start_age = "and I'm also "
    end_name = " years old!"
    print( start_name + ask_name + mid_comma + start_age + ask_age + end_name)


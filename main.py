import re


def parse_int(string):

    # Initializing dictionaries for unique numeric values
    unit_dict = {"hundred": 100, "thousand": 1000, "million": 1000000}
    ones_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
                 "nine": 9}

    ten_dict = {"ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
                "seventeen": 17, "eighteen": 18, "nineteen": 19}
    tens_dict = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80,
                 "ninety": 90}

    # if list(unit_dict.keys())[1] in string:

    return

"""
TODO:

# Check whether there are hundreds or thousands in the number.
# If thousand in number, split based on thousand and convert to string.
# Repeat for hundred if applicable.
* Convert string lists into numerical values and compile into appropriate thousand or hundred value.
* Process remaining values.
* Sum numbers into total sum.
"""

def split_string(string_list):
    for i in range(len(string_list)):
        string_list[i] = string_list[i].strip()
    prior = re.split(" |-", string_list[0])
    post = re.split(" |-", string_list[2])
    split_string = prior + [string_list[1]] + post
    if "and" in split_string:
        split_string.remove("and")  # list of each numeric value from string split by space, excluding any "and"
    return [split_string, prior, [string_list[1]], post]

def thousand_present(string):
    string_list = list(string.partition("thousand"))
    split_string(string_list)
    return

def hundred_present(string):
    string_list = list(string.partition("hundred"))
    split_string(string_list)
    return

def convert_thousand(string):
    return

def convert_hundred(string):
    return
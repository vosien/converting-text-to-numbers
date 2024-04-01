import re

# Initializing dictionaries for unique numeric values
unit_dict = {"hundred": 100, "thousand": 1000, "million": 1000000}
value_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
                 "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
                 "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30,
                 "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}


def parse_int(string):
    if string.lower() == "one million":
        return unit_dict.get("million")
    elif string.lower() in list(value_dict.keys()):
        return value_dict.get(string.lower())
    elif "thousand" in string.lower():
        return thousand_present(string.lower())
    elif "hundred" in string.lower():
        return hundred_present(string.lower())
    else:
        return small_present(string.lower())


"""
TODO:

# Check whether there are hundreds or thousands in the number.
# If thousand in number, split based on thousand and convert to string.
# Repeat for hundred if applicable.
# Convert string lists into numerical values and compile into appropriate value.
    * Hundred: Multiply hundred by single prior value and then add subsequent values:
    * Thousand: Multiply by prior value.
# Process remaining values.
# Sum numbers into total sum.
"""


def split_string(string_list):
    for i in range(len(string_list)):
        string_list[i] = string_list[i].strip()
    prior = re.split(" |-", string_list[0])
    if len(string_list) > 2:
        post = re.split(" |-", string_list[2])
        for j in [prior, post]:
            if "and" in j:
                j.remove("and")
        return [prior, [string_list[1]], post]
    if "and" in prior:
        prior.remove("and")
    return [prior, [string_list[1]]]



def small_split(string):
    return re.split(" |-", string)


def thousand_present(string):
    string_list = [x for x in string.partition("thousand") if x]
    split = split_string(string_list)
    convert = convert_values(split)
    hundred = convert_hundred(convert)
    return convert_thousand(hundred)


def hundred_present(string):
    string_list = [x for x in string.partition("hundred") if x]
    split = split_string(string_list)
    convert = convert_values(split)
    return convert_hundred(convert)


def small_present(string):
    split = small_split(string)
    convert = convert_values(split)
    return sum(convert)


def convert_thousand(values):
    values[0] = values[0]*1000
    values.pop(1)
    return sum(values)


def convert_hundred(values):
    if [1000] in values:
        for i in range(0, len(values), 2):
            if 100 in values[i]:
                index = values[i].index(100)
                actual_value = values[i][index-1]*values[i][index]
                values[i][index] = actual_value
                values[i].pop(index-1)
                values[i] = sum(values[i])
            else:
                values[i] = sum(values[i])
    if [100] in values:
        hun_list = []
        for j in values:
            hun_list += j
        if 100 in hun_list:
            index = hun_list.index(100)
            actual_value = hun_list[index-1]*hun_list[index]
            hun_list[index] = actual_value
            hun_list.pop(index-1)
            hun_list = sum(hun_list)
        else:
            hun_list = sum(hun_list)
        return hun_list
    return values


def convert_values(values):
    if any(isinstance(a, list) for a in values):
        for i in range(len(values)):
            for j in range(len(values[i])):
                if values[i][j] in unit_dict:
                    values[i][j] = unit_dict.get(values[i][j])
                elif values[i][j] in value_dict:
                    values[i][j] = value_dict.get(values[i][j])
    elif any(isinstance(b, str) for b in values):
        for i in range(len(values)):
            values[i] = value_dict.get(values[i])
    return values

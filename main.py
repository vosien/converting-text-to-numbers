import re

def parse_int(string):
    unit_dict = {"hundred": 100, "thousand": 1000}
    ones_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    ten_dict = {"ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
                "seventeen": 17, "eighteen": 18, "nineteen": 19}
    tens_dict = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80,
                 "ninety": 90}

    if list(unit_dict.keys())[1] in string:
        string_list = list(string.partition("thousand"))
        for i in range(len(string_list)):
            string_list[i] = string_list[i].strip()
        thousand_mod_list = re.split(" |-", string_list[0])
    return

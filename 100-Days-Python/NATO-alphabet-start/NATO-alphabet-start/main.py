from numpy.f2py.crackfortran import parse_name_for_bind

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # if row.student ==
    # if row.score == 56:
    #     print(row.student)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


data = pandas.read_csv("nato_phonetic_alphabet.csv")
# data = data.to_dict()
# print(data)
#TODO 1. Create a dictionary in this format:

nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def nato():
    name = input("Your name: ").upper()
    try:
        name_code = [nato_dict[letter] for letter in name]
    except KeyError:
        print("Try again with letters")
        nato()
    else:
        print(name_code)

nato()
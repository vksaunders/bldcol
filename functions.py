# def string_clean_up(str_input):
#
# if str_input == None
#     #if isinstance(str_input, str) != True:
#         return ""
#
#     str_input = str(str_input)
#
#     str_input = str_input.strip()
#
#     str_input = str_input.split()
#
#     results = ""
#
#     str_input = results.join(str_input)
#
#     str_input = str_input.replace(" ,", ",")
#
#     #print(str_input)
#
#     return str_input
#
# nasty_string = "          \n\n\n\n\n\nPRATT\t\t\t\t\t"
#
# clean_string = string_clean_up(nasty_string)
#
# for row in rows:
#
#     #city_name = row[0]
#
#     city_name = string_clean_up(row[0])
#
# print(clean_string)



def add_jpgext(str_input):

    # if str_input == None
    # return""

    str_input = str(str_input)

    str_input = str_input +".jpg"

    return str_input

test_file = "bld0545376"

proper_filename = add_jpgext(test_file)

print(proper_filename)

# for row in rows:
#
#     jpg_file = add_jpgext(row[0])

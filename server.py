import re


input_data = input("Server is ready. You can type intergers and then click [ENTER].  Clients will show the mean, median, and mode of the input values.\n")
data = input_data.strip().split()
parsed_data = []
pattern = '^\d+$'
for string_input in data:
    if not re.fullmatch(pattern, string_input):
        break
    parsed_data.append(int(string_input))

if len(data) != len(parsed_data):
    print('please input integer only')

"""
Day 24 - Files, Directories, Other
"""

# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# # Best practice is to close the file manually to ensure highest performance
# file.close()


# Using the with keyword, you can open a file given a variable name
# This method of file management will automatically close the file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Various methods for opening and writing to a file. w with erase and overwrite, a will append
# with open("my_file.txt", "a") as file:
#     file.write("Writing a new line\n")
#
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Absolute file paths will start with /, relative will take navigation from the working directory

# Mail Merge File - take the names from the input directory and the letter_template and return new documents in the
# output directory replacing the templated value

with open("Input/names.txt") as names:
    names_array = names.read().splitlines()

with open("Input/letter_template.txt") as letter_template:
    template_content = letter_template.read()

for name in names_array:
    with open(f"Output/{name}.txt", "w") as letter:
        letter_content = template_content.replace("[name]", name)
        letter.write(letter_content)
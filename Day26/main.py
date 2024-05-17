"""
Comprehensions - Create a new list from a previous list

new_list = [new_item_expression for item in old_list]
"""

name = input("Enter a name: ").lower()
nato_alphabet = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "White", "Xavier", "Yankee", "Zulu"]
nato_list = [nato_alphabet[ord(letter) - 97] for letter in name]
print(nato_list)
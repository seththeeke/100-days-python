"""
Day 25 - Reading files from CSV w/Pandas
"""

# with open("weather_data.csv") as file:
#     csv_data = file.readlines()

# import csv
#
# with open("weather_data.csv") as file:
#     csv_data = csv.reader(file)
#     for row in csv_data:
#         print(row)

# https://pandas.pydata.org/
import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

# Pandas CSV Data is Broken into Series and Data Frames

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
# Pandas has a number of built in data analysis functions
print(data["temp"].mean())

#  You can fetch rows, columns by a condition
print(data[data.day == "Monday"])

# Create data frame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [20, 30, 40]
}
to_pandas = pandas.DataFrame(data_dict)
to_pandas.to_csv("data.csv")


# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()


#Without Pandas
# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     next(data)
#     temperatures = []
#     for row in data:
#         temperatures.append(int(row[1]))
#     print(temperatures)

#With Pandas
import pandas

# data = pandas.read_csv("weather_data.csv")
# # temperatures = data["temp"]
# data_dict = data.to_dict()
# print(data_dict)
#
# temperatures = data["temp"].to_list()
# print(temperatures)
#
# #CHALLENGE: calculate avg temperature
# average_temp = round(sum(temperatures) / len(temperatures), 2)
# print(average_temp)
#
# #With Pandas:
# average = round(data["temp"].mean(), 2)
# print(average)
#
# #CHALLENGE: Find max temp value
# max_value = data["temp"].max()
# print(max_value)
#
# #Get Data in Columns
# print(data["condition"])
# #or
# print(data.condition)
#
# #Get Data in Rows
# monday = data[data.day == "Monday"]
# print(monday)
#
# #CHALLENGE: Pull row of data when the temperature is at the max
# max_temp_row = data[data.temp == data.temp.max()]
# print(max_temp_row)
#
# #Pull values in the row
# tuesday_row = data[data.day == "Tuesday"]
# print(tuesday_row.condition)
#
# #CHALLENGE: Get Wednesday's temperature and convert it into Fahrenheit
# wednesday_fahrenheit = data[data.day == "Wednesday"].temp * 9/5 + 32
# print(f"{wednesday_fahrenheit}")
#
# #Create a DataFrame from scratch
# data_dict = {
#     "students": ["Amie", "James", "Angela"],
#     "scores": [76, 56, 75]
# }
# pandas_data = pandas.DataFrame(data_dict)
# print(pandas_data)
# csv_data = data.to_csv("new_data.csv")


#SQUIRREL CHALLENGE: count how many Grey, Red, Black squirrel are there, build new DataFrame and export it in csv
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# color_occurrences = data.groupby(['Primary Fur Color']).size()
# squirrels_color_data = pandas.DataFrame(color_occurrences)
# sqrl_csv_data = squirrels_color_data.to_csv("sqrl_data.csv")

#Teacher's solution
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
data_dict = {
    "Colors": ["Gray", "Red", "Black"],
    "Totals": [gray_squirrels, red_squirrels, black_squirrels]
}
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("second_sqrl_data.csv")






# Name: Bhoomika M N
# Project: Personal Information Manager
# Description: A Python program that stores and displays personal information.

# -----------------------------------
# Welcome Message
# -----------------------------------

print("===================================")
print(" Welcome to Personal Info Manager ")
print("===================================\n")

# -----------------------------------
# Static Information
# -----------------------------------

# Storing personal details
name = "Bhoomika"
age = 21
city = "Shimoga"
hobby = "Web Designing"

# Calculating age in months
age_in_months = age * 12

# -----------------------------------
# User Input Section
# -----------------------------------

# Getting favorite food from user
favorite_food = input("Enter your favorite food: ").strip()

# Validation for empty input
while favorite_food == "":
    print("Favorite food cannot be empty.")
    favorite_food = input("Please enter your favorite food: ").strip()

# Getting favorite color from user
favorite_color = input("Enter your favorite color: ").strip()

# Validation for empty input
while favorite_color == "":
    print("Favorite color cannot be empty.")
    favorite_color = input("Please enter your favorite color: ").strip()

# -----------------------------------
# Formatting Data
# -----------------------------------

formatted_name = name.title()
formatted_city = city.title()
formatted_hobby = hobby.title()
formatted_food = favorite_food.title()
formatted_color = favorite_color.capitalize()

# -----------------------------------
# Displaying Information
# -----------------------------------

print("\n===================================")
print("      PERSONAL INFORMATION         ")
print("===================================")

print(f"Name           : {formatted_name}")
print(f"Age            : {age} years")
print(f"Age in Months  : {age_in_months} months")
print(f"City           : {formatted_city}")
print(f"Hobby          : {formatted_hobby}")
print(f"Favorite Food  : {formatted_food}")
print(f"Favorite Color : {formatted_color}")

print("===================================")

# -----------------------------------
# Goodbye Message
# -----------------------------------

print("\nThank you for using the program!")
print("Have a great day!")
# # Datatypes

# # Strings
# print("Hello"[4])  # print the letter in the position 4
# print("hello" + "world")  # concatanate words

# # Integer -> print(123 + 345)
# # Float -> print(3.14159)
# # Boolean -> True False

# PEMDAS (Left -> Right)
# ()    Parentheses
# **    Exponentes
# *     Multiplication
# /     Division
# +     Addition
# -     Subtraction

# Data Type Exercises
# Instructions
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
two_digit_number = input("Type a two digit number: ")
sum = int(two_digit_number[0]) + int(two_digit_number[1])
print(sum)

# Round Function
print(round(8 / 3, 3))

# f-strings
score = 0
print(f"Your score is {score}")

# Exercises

# BMI-Calculation
import math

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# bmi = int(weight / (pow(height, 2)))
bmi = int(weight / (height**2))
print(bmi)

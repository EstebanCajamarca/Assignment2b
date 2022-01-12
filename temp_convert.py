# Author: Esteban Cajamarca
# GitHub username: EstebanCajamarca
# Date: 1/11/2022
# Description: Write a program that converts Celsius temperatures to Fahrenheit temperatures.
# The formula is:
#
# F = (9/5)C + 32
#
# where F is the Fahrenheit temperature and C is the Celsius temperature.
# The program should prompt the user to input a Celsius temperature and should display the
# corresponding Fahrenheit temperature. It should display only the converted temperature on
# its own line without additional text (such as an 'F').

print("Please enter a Celsius temperature.")
cel_temp = float(input())
print("The equivalent Fahrenheit temperature is:")
print('{0:.4g}'.format(float((9/5) * cel_temp + 32)))


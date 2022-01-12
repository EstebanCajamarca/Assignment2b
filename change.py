# Author: Esteban Cajamarca
# GitHub username: EstebanCajamarca
# Date: 1/11/2022
# Description: Write a program that asks the user for a (integer)
# number of cents, from 0 to 99, and outputs how many of each type
# of coin would represent that amount with the fewest total number of coins.

print("Please enter an amount in cents less than a dollar.")
change = int(input())
Q = int(change / 25)
D = int((change - Q * 25) / 10)
N = int((change - (Q * 25) - (D * 10)) / 5)
P = int((change - (Q * 25) - (D * 10) - (N * 5)) / 1)
print("Your change will be:")
print("Q:", Q)
print("D:", D)
print("N:", N)
print("P:", P)

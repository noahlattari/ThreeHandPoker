import sys

lines = []
number_of_hands = input()
for i in range(int(number_of_hands)):
    lines+=input().replace("\n", "").split(" ")
print (lines)
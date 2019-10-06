import sys, io


mappings = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
bestHand = []
lines = []
number_of_hands = input()

def highCard( hand ):
   return max(mappings.get(hand[1][0]), mappings.get(hand[2][0]), mappings.get(hand[3][0]))

def flush( hand ):
   return mappings.get(hand[1][1]) == mappings.get(hand[2][1]) and mappings.get(hand[2][1]) == mappings.get(hand[3][1])

def straight(hand):
    x = mappings.get(hand[1][0])
    y = mappings.get(hand[2][0])
    z = mappings.get(hand[3][0])
    if (x + 1 == y and y + 1 == z) or (x + 1 == z and z + 1 == y) or (y + 1 == z and z + 1 == x) or (y + 1 == x and x + 1 == z) or (z + 1 == y and y + 1 == x) or (z + 1 == x and x + 1 == y):
        return True
   
def threeOfAKind(hand):
   return mappings.get(hand[1][0]) == mappings.get(hand[2][0]) and mappings.get(hand[2][0]) == mappings.get(hand[3][0])

def pair(hand):
   x = mappings.get(hand[1][0])
   y = mappings.get(hand[2][0])
   z = mappings.get(hand[3][0])
   if (x == y or x == z or y == z):
      return True

#returns an int based on the hand power
def handType(hand):
    if flush(hand) and straight(hand):
        return 5
    elif threeOfAKind(hand):
        return 4
    elif straight(hand):
        return 3
    elif flush(hand):
        return 2
    elif pair(hand):
        return 1
    else:
        return 0


for i in range(int(number_of_hands)):
    lines+=input().replace("\n", "").split(" ")

bestHand = [ lines[0], lines[1], lines[2], lines[3] ]



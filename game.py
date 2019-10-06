import sys, io

#Map each card to their numerical value for future comparisons.
mappings = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
bestHand = []
lines = []
#The number of hands we have is the first input.
number_of_hands = input()

#Determines the greatest numbered card in a hand.
def highCard( hand ):
   return max(mappings.get(hand[1][0]), mappings.get(hand[2][0]), mappings.get(hand[3][0]))

#Determines if a hand is a flush.
def flush( hand ):
   return hand[1][1] == hand[2][1] and hand[2][1] == hand[3][1]

#Determines if a hand is a straight.
def straight(hand):
    x = mappings.get(hand[1][0])
    y = mappings.get(hand[2][0])
    z = mappings.get(hand[3][0])
    if ( (x + 1) == y and (y + 1) == z) or ( (x + 1) == z and (z + 1) == y) or ( (y + 1) == z and (z + 1) == x) or ( (y + 1) == x and (x + 1) == z) or ( (z + 1) == y and (y + 1) == x) or ( (z + 1) == x and (x + 1) == y):
        return True

#Determines if a hand is a three of a kind.
def threeOfAKind(hand):
   return mappings.get(hand[1][0]) == mappings.get(hand[2][0]) and mappings.get(hand[2][0]) == mappings.get(hand[3][0])

#Determines if a hand is a pair.
def pair(hand):
   x = mappings.get(hand[1][0])
   y = mappings.get(hand[2][0])
   z = mappings.get(hand[3][0])
   if (x == y or x == z or y == z):
      return True

#Returns an integer based on how strong the hand is. i.e Straight Flush returns the highest power.
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

#Read in all the hands well formated.
for i in range(int(number_of_hands)):
    lines+=input().replace("\n", "").split(" ")

#Set the current best hand as the first hand/
bestHand = [ lines[0], lines[1], lines[2], lines[3] ]
ties = []

#A hand is every 4 entries.
for i in range( 0, (len(lines)) - 4, 4 ):

   hand = [ lines[i + 4], lines[i + 5], lines[i + 6], lines[i + 7] ]

   #Case1: The current hand is better than our current best hand, update the best hand.
   if(handType(hand) > handType(bestHand)):
      bestHand = hand
      ties = []
   #Case2: The current hand and best hand are equal.
   elif(handType(hand) == handType(bestHand)):
      #Case2.2: They are equal but one has a higher numerical value.
      if(highCard(hand) > highCard(bestHand)):
         bestHand = hand
         ties = []
      #Case3: They are equal and have the same numerical values, tie.
      elif(highCard(hand) == highCard(bestHand)):
         ties.append(hand[0])
         ties.append(bestHand[0])

#If the ties array is empty, we have no ties, so print the best hand.
if (len(ties) == 0):
   print(bestHand[0])
#If it isn't empty, we have a tie. Print all the ties.
else:
   res = ""
   ties.sort()
   for i in range(len(ties)):
      res += ties[i] + " "
   print(res)


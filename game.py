mappings = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
#print(mappings.get('T'))


bestHand = []
lines = []
hands = input()
for i in range(int(hands)):
    lines+=input().replace("\n", "").split(" ")

bestHand = lines[0] + lines[1] + lines[2] + lines[3] 

#for i in range( int(lines) / hands - 1) :


def highCard( hand ):
    # hand = x1y2z3
    if (hand[0])

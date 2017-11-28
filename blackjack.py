#initial version of terminal Blackjack game, no OOP
#only hit and stay
#standard 52 cards deck
    #Suits: Hearts, Diamond, Clubs, Spades ♥♦♣♠
    #2-10 face value
    #J, Q, K equals 10
    #ace based on player's decesion

import random

card_value = {'♥2' : 2, '♥3' : 3, '♥4' : 4, '♥5' : 5, '♥6' : 6, '♥7' : 7, '♥8' : 8, '♥9' : 9, '♥10' : 10, '♥J' : 10,
'♥Q' : 10, '♥K' : 10, '♥A' : 11, '♦2' : 2, '♦3' : 3, '♦4' : 4, '♦5' : 5, '♦6' : 6, '♦7' : 7, '♦8' : 8, '♦9' : 9,
'♦10' : 10, '♦J' : 10, '♦Q' : 10, '♦K' : 10, '♦A' : 11,'♣2': 2, '♣3' : 3, '♣4' : 4, '♣5' : 5, '♣6' : 6, '♣7' : 7,
'♣8' : 8, '♣9' : 9,'♣10' : 10, '♣J' : 10, '♣Q' : 10, '♣K' : 10, '♣A' : 11, '♠2' : 2, '♠3' : 3, '♠4' : 4, '♠5' : 5,
'♠6' : 6, '♠7' : 7, '♠8' : 8, '♠9' : 9, '♠10' : 10, '♠J' : 10, '♠Q' : 10, '♠K' : 10, '♠A' : 11}

#create deck
deck = []
for suit in ['♥', '♦', '♣', '♠']:
    for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
        deck.append(suit + rank)
random.shuffle(deck)

dealer_cards = []
player_cards = []
ace_count = {'player_1valued_aces': 0, 'dealer_1valued_aces': 0}

#two cards to the player and two card to the Dealer
def create_hands():
    while len(dealer_cards) != 2:
        dealer_cards.append(deck.pop())
        if len(dealer_cards) == 2:
            print("The Dealer has the following cards: XX and  ", dealer_cards[1])

    while len(player_cards) != 2:
        player_cards.append(deck.pop())
        if len(player_cards) == 2:
            print("The Player has the following cards:  ", player_cards)

#check double aces
    if sum(map(card_value.get, dealer_cards)) == 22:
        ace_count['dealer_1valued_aces'] += 1
    elif sum(map(card_value.get, player_cards)) == 22:
        print("Note: your second ace is valued as 1!")
        ace_count['player_1valued_aces'] += 1

#check for natural blackjack
    elif sum(map(card_value.get, dealer_cards)) == 21:
        print("Dealer wins!")
    elif sum(map(card_value.get, player_cards)) == 21:
        print("Player wins!")
    else:
        player_dec()

#check for player decesion
def player_dec():
    print("""
    Use the following keys to continue:
     H: Hit
     S: Stand
     """)
    choice = input("> ")
    if choice == "H":
        hit()
    elif choice == "S":
        dealer_hand()

#check the winner
def winner():
    player_points = sum(map(card_value.get, player_cards)) - (ace_count['player_1valued_aces'] * 10)
    dealer_points = sum(map(card_value.get, dealer_cards)) - (ace_count['dealer_1valued_aces'] * 10)

    if player_points > 21:
        print("BUSTED!!!")
        print("The Dealer has the total of  " + str(dealer_points) +" from the following cards:", dealer_cards)
        print("The Player has the total of  " + str(player_points) +" from the following cards:", player_cards)

    elif dealer_points > 21:
        print("The Dealer has the total of  " + str(dealer_points) +" from the following cards:", dealer_cards)
        print("The Player has the total of  " + str(player_points) +" from the following cards:", player_cards)
        print("Dealer BUSTED! Player wins!!!")

    elif player_points > dealer_points:
        print("The Dealer has the total of  " + str(dealer_points) +" from the following cards:", dealer_cards)
        print("The Player has the total of  " + str(player_points) +" from the following cards:", player_cards)
        print("Player wins!!!")

    elif player_points < dealer_points:
        print("The Dealer has the total of  " + str(dealer_points) +" from the following cards:", dealer_cards)
        print("The Player has the total of  " + str(player_points) +" from the following cards:", player_cards)
        print("Dealer wins!!!")

    elif player_points == dealer_points:
        print("The Dealer has the total of  " + str(dealer_points) +" from the following cards:", dealer_cards)
        print("The Player has the total of  " + str(player_points) +" from the following cards:", player_cards)
        print("PUSH!!!")

def hit():
    player_cards.append(deck.pop())
    #let the player decide how he values ace
    if player_cards[-1] == '♠A' or player_cards[-1] == '♣A' or player_cards[-1] == '♦A' or player_cards[-1] == '♥A':
        print("Aces are valued as either 1 or 11 according to the player's choice")
        ace_input = int(input(" "))
        if ace_input == 1:
            ace_count['player_1valued_aces'] += 1

    print("The Player has the following cards:  ", player_cards)

    if sum(map(card_value.get, player_cards)) - (ace_count['player_1valued_aces'] * 10) >= 21:
        winner()
    else:
        player_dec()

#finish the dealer's hand
def dealer_hand():
    while sum(map(card_value.get, dealer_cards)) - (ace_count['dealer_1valued_aces'] * 10) < 17:
        dealer_cards.append(deck.pop())
        if dealer_cards[-1] == '♠A' or dealer_cards[-1] == '♣A' or dealer_cards[-1] == '♦A' or dealer_cards[-1] == '♥A':
            ace_count['dealer_1valued_aces'] += 1
    winner()



create_hands()

#importing the necessary libraries
from BlackjackPackage.Users import HumanUser, ComputerDealer
from .Aesthetics import Color



#function that initiates the game and holds the logic for winning or losing

def play_the_game():
    user = HumanUser()                          #creating the human player
    computer_dealer = ComputerDealer()          #creating the computer dealer
    
    #verifying how many cards are in the deck at the beginning of the game
    print(f'There are currently {len(user.deck)} cards in the Deck.')
    
    #logic for the Player to ask for another card or not
    while sum(user.cards_in_play) < 21:
        print("\nIt's the Player's turn.")
        hit_or_stay = input('\nhit or stay?\nPlease type the action you want, e.g: hit\nPlayer: ')
        if hit_or_stay.lower() == 'hit':
            user.hit()
        elif hit_or_stay.lower() == 'stay':
            break
    
    #demarcate the end of the Player's turn from the beginning of the Computer dealer's
    print(Color.BOLD + Color.PURPLE + '*--------------------------------------------*' + Color.END)
    
    #logic for the computer dealer to pick another card or not
    while (sum(computer_dealer.cards_in_play) < 21):
        print("\nIt's the Dealer's turn.")
        if sum(user.cards_in_play) >= 21:
            print("Dealer: I don't need to play.")
            break
        if(sum(computer_dealer.cards_in_play) > sum(user.cards_in_play)):
            break
        else:
            computer_dealer.hit()
    
    #defining the conditions to win a game
    def win_logic():
        if sum(user.cards_in_play) == 21:
            return True
        if sum(computer_dealer.cards_in_play) > 21:
            return True
        if(sum(computer_dealer.cards_in_play) < sum(user.cards_in_play)) and (sum(user.cards_in_play) < 21):
            return True
        
    print(f"Your total = {sum(user.cards_in_play)}")
    print(f"Computer's total = {sum(computer_dealer.cards_in_play)}")
    
    if win_logic():
        user.win()                      #if user satisfies one of the conditions to win a game, call its win method
    else:
        computer_dealer.win()
    
    computer_dealer.reset_deck()        #reset the deck back to 52 cards
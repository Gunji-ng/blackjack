#importing the necessary libraries
import random
from .Aesthetics import Color



# a class that initializes the deck and the game's actions

class Play():
    
    #creating a deck containing 52 cards
    
    deck = [i for i in range(1,11)] * 4    # 4 variants of cards A-10 (gives us 40 cards)
    
    deck.extend([10,10,10]*4)              # cards with faces (Kings, Queens & Jacks) are taken as 10 (12 of them in total)
    
    random.shuffle(deck)                   # shuffling the deck so that the sequence of the cards is randomized
        
    
    def __init__(self):
        self.cards_in_play = []            #these are the cards a player currently has
        print('Player Created!')
    
    
    def hit(self):
        """
        Represents the 'hit' action, whereby the Player is dealt another card.
        """
        card_index = random.randint(0, len(Play.deck)-1)
        
        self.cards_in_play.append(Play.deck[card_index])        #the card dealt is added to those already with the player
        
        Play.deck.pop(card_index)                               #removing the card dealt from the deck
        
        print(Color.BOLD + f'Current total is: {sum(self.cards_in_play)}' + Color.END)
    
    
    def stay(self):
        """
        Does nothing. Signifies that the Player is satisfied with his/her current total.
        """
        pass
        
    
    def reset_deck(self):
        """
        Method is called at the end of each game to reset the deck back to 52 cards.
        """
        Play.deck = [i for i in range(1,11)] * 4
        Play.deck.extend([10,10,10]*4)
        random.shuffle(Play.deck)



#class for human player object

class HumanUser(Play):
    
    def __init__(self):
        self.cards_in_play = []
        print('User Player Created!')
    
    def win(self):
        print(Color.BOLD + Color.BLUE + 'Congratulations!!! You win!' + Color.END)
        

        
#class for computer dealer object

class ComputerDealer(Play):
    
    def __init__(self):
        self.cards_in_play = []
        print('Computer Player Created!')
    
    def win(self):
        print(Color.BOLD + Color.RED + 'You lose!' + Color.END)
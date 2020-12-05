from ..BlackjackPackage.Users import HumanUser, ComputerDealer
import pytest

#new HumanUser object to be passed to the test functions for the human user
@pytest.fixture
def test_user():
    user = HumanUser()
    user.reset_deck()
    return user

#new ComputerDealer object to be passed to the test functions for the computer dealer
@pytest.fixture
def comp_dealer():
    dealer = ComputerDealer()
    dealer.reset_deck()
    return dealer

#test if the number of cards in the deck is 52 at initialization
@pytest.mark.deck
def test_init_cards_in_deck_length(test_user):
    assert len(test_user.deck) == 52

#test if the user's cards in play is empty at initialization
@pytest.mark.deck
def test_init_cards_in_play_length(test_user):
    assert len(test_user.cards_in_play) == 0

#test if we have the expected number of occurences of each card in the deck at initialization
@pytest.mark.deck
def test_number_occurences_in_deck(test_user):
    #testing for occurences of cards 1-9
    for i in range(1,10):
        assert test_user.deck.count(i) == 4
    #testing for occurences of the number 10
    #remember that the cards with faces are taken as 10 and that they are twelve in total
    #adding the twelve cards with faces to the four cards that are actually 10, we expect 16 occurences
    assert test_user.deck.count(10) == 16

#test if length of the deck reduces by 1 card when hit() is called once
@pytest.mark.human_user
def test_deck_length_after_one_hit(test_user):
    test_user.hit()
    assert len(test_user.deck) == 51

#test if length of the deck reduces by 2 cards when hit() is called twice
@pytest.mark.human_user
def test_deck_length_after_two_hits(test_user):
    for i in range(2):
        test_user.hit()
    assert len(test_user.deck) == 50

#test if length of the deck reduces by 5 cards when hit() is called five times
@pytest.mark.human_user
def test_deck_length_after_five_hits(test_user):
    for i in range(5):
        test_user.hit()
    assert len(test_user.deck) == 47

#test if a card is added to the user's cards in play when hit() is called once
@pytest.mark.human_user
def test_cards_in_play_length_after_one_hit(test_user):
    test_user.hit()
    assert len(test_user.cards_in_play) == 1

#test if 2 cards are added to the user's cards in play when hit() is called twice
@pytest.mark.human_user
def test_cards_in_play_length_after_two_hits(test_user):
    for i in range(2):
        test_user.hit()
    assert len(test_user.cards_in_play) == 2

#test if 5 cards are added to the user's cards in play when hit() is called five times
@pytest.mark.human_user
def test_cards_in_play_length_after_five_hits(test_user):
    for i in range(5):
        test_user.hit()
    assert len(test_user.cards_in_play) == 5

#test if reset_deck() resets the deck back to its initial length after some cards have been removed
def test_reset_deck(test_user):
    for i in range(3):
        test_user.hit()
    #test to ensure 3 cards have been removed from the deck and added to the user's cards in play
    assert len(test_user.deck) == 49
    assert len(test_user.cards_in_play) == 3
    #reset the deck
    test_user.reset_deck()
    #test if cards have been restored
    assert len(test_user.deck) == 52

#test if length of the deck reduces by 1 card when ComputerDealer calls hit() once
@pytest.mark.computer_dealer
def test_computer_dealer_deck_length_after_one_hit(comp_dealer):
    comp_dealer.hit()
    assert len(comp_dealer.deck) == 51

#test if length of the deck reduces by 5 card when ComputerDealer calls hit() five times
@pytest.mark.computer_dealer
def test_computer_dealer_deck_length_after_five_hits(comp_dealer):
    for i in range(5):
        comp_dealer.hit()
    assert len(comp_dealer.deck) == 47

#test if a card is added to the computer dealer's cards in play when ComputerDealer calls hit() once
@pytest.mark.computer_dealer
def test_computer_dealer_cards_in_play_length_after_one_hit(comp_dealer):
    comp_dealer.hit()
    assert len(comp_dealer.cards_in_play) == 1

#test if 5 cards are added to the computer dealer's cards in play when ComputerDealer calls hit() five times
@pytest.mark.computer_dealer
def test_computer_dealer_cards_in_play_length_after_one_hit(comp_dealer):
    for i in range(5):
        comp_dealer.hit()
    assert len(comp_dealer.cards_in_play) == 5

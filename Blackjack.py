import random
import os
from Art import Blackjack_logo

def number_list_adder(list_name):
    """This function only add the elements of the list having only  'int' datatype"""
    
    if sum(list_name)==21 and len(list_name)==2:
        return 0
    elif 11 in list_name and sum(list_name)>21 :
        list_name.remove(11)
        list_name.append(1) 
    return sum(list_name)

def score_compare(score1,score2):
    if score1==score2:
        return "Draw 😁"
    elif score1==0:
        return "You won! you have Blackjack"
    elif score2==0:
        return "You lose! opponent have Blackjack"
    elif score1>21:
        return "you lose"
    elif score2>21:
        return "You won"
    elif score1>score2:
        return " YOU WON"
    elif score2>score1:
        return " You lose"
    


def blackjack():
    print(Blackjack_logo)
    number_lisr = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    player_cards=[]
    computer_cards=[]

    for i in range(2):
        player_cards.append(random.choice(number_lisr))
        computer_cards.append(random.choice(number_lisr))

    user_ask="yes"

    while user_ask== "yes":
        print("     Your card:",player_cards,"Your total score is",number_list_adder(player_cards))
        print("     Computer first card is :",computer_cards[0])

        if number_list_adder(player_cards)== 0 or number_list_adder(computer_cards)==0 or number_list_adder(player_cards)>21:
            user_ask="no"
        else:
            user_ask=str(input("type 'yes' to get another card, or type 'no' for pass: ")).lower()
            if user_ask=="yes":
                player_cards.append(random.choice(number_lisr))
            else:
                user_ask="no"

    while number_list_adder(computer_cards)!=0 and number_list_adder(computer_cards)<17:
        computer_cards.append(random.choice(number_lisr))
    print(f"Your final cards are:{player_cards} and total score is {number_list_adder(player_cards)}")
    print(f"computer final cards are:{computer_cards} and total score is {number_list_adder(computer_cards)}")

    print(score_compare(number_list_adder(player_cards),number_list_adder(computer_cards)))


while input("Do you want to play game (yes/no): ").lower()=="yes":
    os.system("cls")
    
    blackjack()

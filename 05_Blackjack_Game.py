import random
import os

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♠', '♥', '♦', '♣']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}


def play_game():
    print("""      ╔╗ ╦  ╔═╗╔═╗╦╔═ ╦╔═╗╔═╗╦╔═
      ╠╩╗║  ╠═╣║  ╠╩╗ ║╠═╣║  ╠╩╗
      ╚═╝╩═╝╩ ╩╚═╝╩ ╩╚╝╩ ╩╚═╝╩ ╩
      ╔╗ ┬ ┬  ╔═╗┌┬┐┌─┐┌─┐┌─┐┌┐┌
      ╠╩╗└┬┘  ╚═╗ │ ├┤ ├┤ ├─┤│││
      ╚═╝ ┴   ╚═╝ ┴ └─┘└  ┴ ┴┘└┘  """)
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    player_hand = []
    dealer_hand = []
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_value = sum([values[rank] for rank, suit in player_hand])
    dealer_value = sum([values[rank] for rank, suit in dealer_hand])
    p_h = ""
    d_h = ""
    for a in player_hand:
        p_h += a[0] + a[1] + " "
    for b in dealer_hand:
        d_h += b[0] + b[1] + " "

    print(f"{'-' * 39}\n   Your Hand: {p_h} (Your Score:   {player_value})")
    print(f""" Dealer Hand: {d_h} (Dealer Score: {dealer_value})\n{'-' * 39}\n                         .------.
      .------.           |A .   |
      |A_  _ |    .------; / \  |
      |( \/ )|-----. _   |(_,_) |
      | \  / | /\  |( )  |  I  A|
      |  \/ A|/  \ |_x_) |------'
      `-----+'\  / | Y  A|
            |  \/ A|-----' 
            `------'""")
    if player_value == 21:
        print('Blackjack! You win!')
        while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
            os.system('cls' if os.name == 'nt' else 'clear')
            play_game()
    if dealer_value == 21:
        print(""" Dealer has Blackjack!    
 __   _____  _   _    _    ___  ___ ___ 
 \ \ / / _ \| | | |  | |  / _ \/ __| __|
  \ V / (_) | |_| |  | |_| (_) \__ \ _| 
   |_| \___/ \___/   |____\___/|___/___|                                                                        
""")
        while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == "y":
            os.system('cls' if os.name == 'nt' else 'clear')
            play_game()
    while True:
        action = input("Do you want to (h)it or (s)tand? (h/s): ")
        if action == 'h':
            player_hand.append(deck.pop())
            player_value = sum([values[rank] for rank, suit in player_hand])
            p_h = ""
            for a in player_hand:
                p_h += a[0] + a[1] + " "
            print(f"{'-' * 39}\n   Your Hand: {p_h}(Your Score: {player_value})")
            print(f" Dealer Hand: {d_h} (Dealer Score: {dealer_value})\n{'-' * 39}")
            if player_value > 21:
                print(""" You went over 21.   
 __   _____  _   _    _    ___  ___ ___ 
 \ \ / / _ \| | | |  | |  / _ \/ __| __|
  \ V / (_) | |_| |  | |_| (_) \__ \ _| 
   |_| \___/ \___/   |____\___/|___/___|                                                                         
""")
                while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    play_game()
        elif action == 's':
            break
    while True:
        if dealer_value < 17:
            dealer_hand.append(deck.pop())
            dealer_value = sum([values[rank] for rank, suit in dealer_hand])
            d_h = ""
            for b in dealer_hand:
                d_h += b[0] + b[1] + " "
            print(f"Dealer Hand: {d_h} (Dealer Score is: {dealer_value})\n{'-' * 39}")
            if dealer_value > 21:
                print(""" Dealer went over 21.
 __   _____  _   _   __      _____ _  _ 
 \ \ / / _ \| | | |  \ \    / /_ _| \| |
  \ V / (_) | |_| |   \ \/\/ / | || .` |
   |_| \___/ \___/     \_/\_/ |___|_|\_|
""")

                while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    play_game()
        else:
            break

    if player_value > dealer_value:
        print(""" You have a higher value than the dealer.
 __   _____  _   _   __      _____ _  _ 
 \ \ / / _ \| | | |  \ \    / /_ _| \| |
  \ V / (_) | |_| |   \ \/\/ / | || .` |
   |_| \___/ \___/     \_/\_/ |___|_|\_|
""")
    elif player_value < dealer_value:
        print(""" The dealer has a higher value than you.    
 __   _____  _   _    _    ___  ___ ___ 
 \ \ / / _ \| | | |  | |  / _ \/ __| __|
  \ V / (_) | |_| |  | |_| (_) \__ \ _| 
   |_| \___/ \___/   |____\___/|___/___|                                                                         
""")
    else:
        print("""You have the same value as the dealer.
  ___ _____ ___    ___  ___    ___      __
 |_ _|_   _/ __|  |   \| _ \  /_\ \    / /
  | |  | | \__ \  | |) |   / / _ \ \/\/ / 
 |___| |_| |___/  |___/|_|_\/_/ \_\_/\_/  
""")


os.system('cls' if os.name == 'nt' else 'clear')
play_game()

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls' if os.name == 'nt' else 'clear')
    play_game()

from shlex import join

import numpy as  np

suit = ['H', 'D', 'C', 'S']
rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card  = {"suit":"suits", "rank":"ranks"}
deck = []
for s in suit:
    for r in rank:
        card = {"suit":s, "rank":r}
        deck.append(card)

np.random.shuffle(deck)

player= {"name": "Player 1", "hand": [],"chips":1000,"current_bet":0,"folded":False,"all_in":False,"hand_rank":0}

def deal_hand(player, deck):
    player["hand"] = deck[:2]
    del deck[:2]

player_count = 0
print("Welcome to the table please select the number of players playing (2-4): ")
player_count = int(input())
#The dealing of cards according to the num of players
def deal_holes(player_count,deck):
    players = []
    for i in range(player_count):
        player = {"name": f"Player {i+1}", "hand": [],"chips":1000,"current_bet":0,"folded":False,"all_in":False,"hand type":"classified","hand ranking":0}
        deal_hand(player, deck)
        players.append(player)
    return players
players = deal_holes(player_count,deck)


choice = ["fold", "call", "check", "raise"]#actions
#The Action taking fuction
def player_action(player):
    print(f"{player['name']}, your hand is: {player['hand']}")
    print("Choose your action: fold, call, check, raise")
    action = input().lower()
    while action not in choice:
        print("Invalid choice. Please choose fold, call, check, or raise.")
        action = input().lower()
    return action

def player_status(player):
    for i in player:
        if i["folded"]==True:
            print(f"{i['name']} - Chips: {i['chips']} - Current Bet: {i['current_bet']} ---- Folded")
        if i["all_in"]==True:
            print(f"{i['name']} - Chips: {i['chips']} - Current Bet: {i['current_bet']} ---- All In")
        else:
            print(f"{i['name']} - Chips: {i['chips']} - Current Bet: {i['current_bet']}")
def deal_community_cards(deck, phase):
    if phase == "flop":
        community_cards = deck[:3]
        del deck[:3]
    elif phase == "turn":
        community_cards = deck[:1]
        del deck[:1]
    elif phase == "river":
        community_cards = deck[:1]
        del deck[:1]
    return community_cards

def Playerwise_display(player, ongoing_bet, pot, community_cards, player_cards):
    print(f"{player['name']} - Chips: {player['chips']} \nCurrent Bet: {ongoing_bet}\nPot: {pot}")
    print("Community Cards:", " ".join([f"{c['rank']}{c['suit']}" for c in community_cards]))
    print("Your Cards:", " ".join([f"{c['rank']}{c['suit']}" for c in player_cards]))

pot = 0;
ongoing_bet = 0;
rank_order = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

community_cards = deal_community_cards(deck, "flop")
def overall_hand(community_cards, player_cards,rank_order):
    all_cards = community_cards + player_cards
    for card in all_cards:
        card["rank_value"] = rank_order[card["rank"]]
    all_cards = sorted(all_cards, key=lambda x: x["rank_value"], reverse=True)
    return all_cards

all_cards = overall_hand(community_cards, players[0]["hand"], rank_order)

def alllcards_dict(all_cards):
    all_cards_dict = {}
    for card in all_cards:
        rank = card["rank"]
        suit = card["suit"]
        if rank in all_cards_dict:
            all_cards_dict[rank].append(suit)
        else:
            all_cards_dict[rank] = [suit]
    return all_cards_dict
all_cards_dict = alllcards_dict(all_cards)
def pair(all_cards,rank_order):
    rank_counts = {}
    for card in all_cards:
        rank = card["rank"]
        if rank in rank_counts:
            rank_counts[rank] += 1
        else:
            rank_counts[rank] = 1
    pairs =[]
    for rank, count in rank_counts.items():
        if count == 2:
            pairs.append(rank)
    return pairs
test = cards = [
    {"rank":"A ","suit":"H"},
    {"rank":"2","suit":"D"},
    {"rank":"3","suit":"C"},
    {"rank":"4","suit":"S"},
    {"rank":"5","suit":"H"}
]

def three_of_a_kind(all_cards,rank_order):
    rank_counts = {}
    for card in all_cards:
        rank = card["rank"]
        if rank in rank_counts:
            rank_counts[rank] += 1
        else:
            rank_counts[rank] = 1
    three_of_a_kind = []
    for rank, count in rank_counts.items():
        if count == 3:
            three_of_a_kind.append(rank)
    return three_of_a_kind 

def four_of_a_kind(all_cards,rank_order):
    rank_counts = {}
    for card in all_cards:
        rank = card["rank"]
        if rank in rank_counts:
            rank_counts[rank] += 1
        else:
            rank_counts[rank] = 1
    four_of_a_kind = []
    for rank, count in rank_counts.items():
        if count == 4:
            four_of_a_kind.append(rank)
    return four_of_a_kind 

def full_house(all_cards,rank_order):
    rank_counts = {}
    for card in all_cards:
        rank = card["rank"]
        if rank in rank_counts:
            rank_counts[rank] += 1
        else:
            rank_counts[rank] = 1
    has_three_of_a_kind = False
    has_pair = False
    for count in rank_counts.values():
        if count == 3:
            has_three_of_a_kind = True
        elif count == 2:
            has_pair = True
    return has_three_of_a_kind and has_pair

def flush(all_cards):
    suit_counts = {}
    for card in all_cards:
        suit = card["suit"]
        if suit in suit_counts:
            suit_counts[suit] += 1
        else:
            suit_counts[suit] = 1
    for count in suit_counts.values(): 
        if count >= 5:
            return True
    return False

def straight(all_cards, rank_order):
    present = [0] * 15
    
    for card in all_cards:
        rank = card["rank"]
        rank_num = rank_order[rank]
        present[rank_num] = 1
        if rank == "A":
            present[1] = 1
            present[14] = 1
    
    # Find consecutive and store ranks
    consecutive = 0
    straight_ranks = []  # Store ranks of straight
    
    for i in range(1, 15):
        if present[i] == 1:
            consecutive += 1
            straight_ranks.append(i)  # Add to list
            if consecutive >= 5:
                # Return the last 5 consecutive ranks
                return True, straight_ranks[-5:]  # ← Return both!
        else:
            consecutive = 0
            straight_ranks = []  # Reset
    
    return False, []
    
print(straight(test,rank_order))





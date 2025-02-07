import random


# Dictionary for suits
SUITS = {
    "Hearts": "\u2665",
    "Diamonds": "\u2666",
    "Clubs": "\u2663",
    "Spades": "\u2660"
}


def create_card():
    """Generates a card with a random value and suit."""
    value = random.randint(2, 11)
    suit = random.choice(list(SUITS.values()))
    card_face = f"[{value}{suit}]"
    return {"value": value, "face": card_face}


def display_rules():
    # displays rules
    """Displays the rules of the game."""
    print("""
    Welcome to Blackjack!
    Rules:
    - The goal is to get as close to 21 as possible without going over.
    - During your turn, you can 'Hit' to draw a card or 'Stay' to end your turn.
    - Face cards (J, Q, K) are worth 10, and Aces are worth 1 or 11.
    - Stay under 21, or lose the game.
    """)


def display_menu():
    """Displays the game menu."""
    print("\nMenu:")
    print("1. Hit")
    print("2. Stay")
    print("3. Display Rules")
    print("4. Display Score")
    print("5. Quit")


def calculate_hand_total(hand):
    """Calculates the total value of a hand."""
    total = 0
    for card in hand:
        total += card["value"]
    return total


def calculate_winner(player_total, dealer_total, player_bust, dealer_bust):
    """
    Determines the winner based on player/dealer totals, and if bust is true.
    Returns the result as a string.
    """
    if player_bust:
        return "Player busts. Dealer wins."
    elif dealer_bust:
        return "Dealer busts. Player wins!"
    elif player_total > dealer_total:
        return "You win!"
    elif player_total < dealer_total:
        return "You lose!"
    else:
        return "It's a tie!"


def save_game_results(player_name, player_hand, dealer_hand, result):
    """Saves the game results to a file using UTF-8 encoding."""
    with open("blackjack_results.txt", "w", encoding="utf-8") as file:  # encoding = utf-8 allows us to write the card special characters to a file, otherwise it'll throw an error since file contents needs to be a string
        file.write("Game Results:\n")
       # writes in result of game in file w/ cards
        player_cards = ""
        for card in player_hand:
            player_cards += card["face"] + " "
        file.write(f"{player_name}'s Hand: {player_cards.strip()}\n")
       
        dealer_cards = ""
        for card in dealer_hand:
            dealer_cards += card["face"] + " "
        file.write(f"Dealer's Hand: {dealer_cards.strip()}\n")
       
        file.write(result + "\n")


def main():
    """
    Deals with user input, showing the result, connecting all the functions, and
    storing variables
    """


    print("Welcome to Blackjack!")
    display_rules()


    # variables to store basic info
    player_name = input("Enter your name: ")
    player_hand = []
    dealer_hand = []
    player_bust = False
    dealer_bust = False
    player_stay = False


    # this is during players turn
    while not player_bust and not player_stay:
        player_cards = ""
        for card in player_hand:
            player_cards += card["face"] + " "
        print(f"\n{player_name}'s Hand: {player_cards.strip()}")
        print(f"Total: {calculate_hand_total(player_hand)}")
        display_menu()
	# checks user input if valid or not
        try:
            choice = int(input("Enter a choice: "))
            if choice == 1:
                card = create_card()
                player_hand.append(card)
                print(f"You drew {card['face']}")
                if calculate_hand_total(player_hand) > 21:
                    player_bust = True
            elif choice == 2:
                player_stay = True
            elif choice == 3:
                display_rules()
            elif choice == 4:
                print(f"Score: Player {calculate_hand_total(player_hand)}, Dealer {calculate_hand_total(dealer_hand)}")
            elif choice == 5:
                print("Thank you for playing! Exiting...")
                return
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number from the menu.")


    # Dealer will draw until its over 17, but this can be adjusted however we want but i think 17 is a good point
    while not dealer_bust and calculate_hand_total(dealer_hand) < 17:
        card = create_card()
        dealer_hand.append(card)
        print(f"Dealer drew {card['face']}")
        if calculate_hand_total(dealer_hand) > 21:
            dealer_bust = True


    # shows results
    player_total = calculate_hand_total(player_hand)
    dealer_total = calculate_hand_total(dealer_hand)
    player_cards = ""
    for card in player_hand:
        player_cards += card["face"] + " "
    dealer_cards = ""
    for card in dealer_hand:
        dealer_cards += card["face"] + " "
    print("\n--- Final Hands ---")
    print(f"{player_name}'s Hand: {player_cards.strip()} (Total: {player_total})")
    print(f"Dealer's Hand: {dealer_cards.strip()} (Total: {dealer_total})")
    print("-------------------")
    result = calculate_winner(player_total, dealer_total, player_bust, dealer_bust)
    print(result)


    # Calls method to save to a file
    save_game_results(player_name, player_hand, dealer_hand, result)


# Runs the code
main()


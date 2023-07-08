import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

'''
Instructions to the game of blackjack

You will get two cards. The dealer also gets two cards. Your task is to get a total closer to 21 than the dealer without going over.
You can say "hit" to get another card or say "stand" on a total and hope that the dealer busts or gets fewer than you.

Once you have ran the code, you are to enter the amount you want to bet, if you bet over the total balance you have the game will send you a error, and tell you to change your betting amount. 
Once you are done betting, please hit the"start game" button to start the game. From there you can click "hit" or "stand" based on your choosing. 
Once you are done playing, you can hit the "quit" button to exit the game.


Instructions to input/output

The inputs to this program are the user entering an amount to bet and clicking on the different buttons(hit, stand, start game, quit, ok).

The outputs to this program will be either updating the user's hand or a pop-up window with one of the following messages based on the users input/program's function: 
"Error, You bet more than you have", "You busted! Your score is " + str(score)", "Dealer busted! You win!", "Dealer wins!", "You win!", ""It's a tie!". 
If the program outputs a window, simply click the "ok" button on the window to exit it.
'''

# function to deal a card
def deal_card(cards):
    card = random.choice(cards)
    return card


# function to calculate the score of a hand
def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score


# list of card values
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

# start game button
def start_game():
    global player_hand, dealer_hand, balance, bet

    bet = int(bet_entry.get())
    if bet > balance:
        messagebox.showinfo("Error", "You bet more than you have")
        return
    player_hand = [deal_card(cards), deal_card(cards)]
    dealer_hand = [deal_card(cards), deal_card(cards)]
    update_labels()

#m main game loop
def main_game(choice):
    global dealer_hand, player_hand

    # if choice is hit
    if choice == "hit":
        player_hand.append(deal_card(cards))
        score = calculate_score(player_hand)
        update_labels()

        if score > 21:
            messagebox.showinfo("Game Over", "You busted! Your score is " + str(score))
            update_balance(-bet)

    # if choice is stand
    else:
        while calculate_score(dealer_hand) < 17:
            dealer_hand.append(deal_card(cards))
            update_labels()

        dealer_score = calculate_score(dealer_hand)
        player_score = calculate_score(player_hand)

        # determines the winner
        if dealer_score > 21:
            messagebox.showinfo("You win!", "Dealer busted! You win!")
            update_balance(bet)

        elif dealer_score > player_score:
            messagebox.showinfo("Dealer wins", "Dealer wins!")
            update_balance(-bet)

        elif dealer_score < player_score:
            messagebox.showinfo("You win!", "You win!")
            update_balance(bet)

        else:
            messagebox.showinfo("It's a tie!", "It's a tie!")

# updates the balance
def update_balance(amount):
    global balance
    balance += amount
    balance_label.config(text="Balance: " + str(balance))

# updates all labels/messages
def update_labels():
    player_hand_label.config(text="Your hand: " + str(player_hand))
    dealer_hand_label.config(text="Dealer's hand: " + str(dealer_hand))


# starting values
balance = 100

# tkinter window
root = tk.Tk()
root.title("Blackjack")

# bet input
bet_label = ttk.Label(root, text="Enter your bet amount:")
bet_label.grid(row=0, column=0)

bet_entry = ttk.Entry(root)
bet_entry.grid(row=0, column=1)

# player's hand
player_hand_label = ttk.Label(root, text="Your hand:")
player_hand_label.grid(row=1, column=0, columnspan=2)

# dealer's hand
dealer_hand_label = ttk.Label(root, text="Dealer's hand:")
dealer_hand_label.grid(row=2, column=0, columnspan=2)

# balance
balance_label = ttk.Label(root, text="Balance: " + str(balance))
balance_label.grid(row=3, column=0, columnspan=2)

# buttons
start_button = ttk.Button(root, text="Start Game", command=start_game)
start_button.grid(row=4, column=0)

hit_button = ttk.Button(root, text="Hit", command=lambda: main_game("hit"))
hit_button.grid(row=5, column=1)

stand_button = ttk.Button(root, text="Stand", command=lambda: main_game("stand"))
stand_button.grid(row=5, column=0)

quit_button = ttk.Button(root, text="Quit", command=root.quit)
quit_button.grid(row=4, column=1)

# start tkinter main loop
root.mainloop()

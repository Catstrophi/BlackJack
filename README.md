# BlackJack
Black Jack game made with tkinter

The code defines a function deal_card that randomly selects a card from a list of card values.
The code defines a function calculate_score that calculates the score of a hand by summing the card values and adjusting for aces (if the score exceeds 21).
The list cards holds the values of the cards.

The code defines a function start_game that is executed when the "Start Game" button is clicked. It handles the initialization of the game, including accepting the bet amount, dealing cards to the player and dealer, and updating the labels.
The code defines a function main_game that is executed when the "Hit" or "Stand" buttons are clicked. It handles the player's choices and updates the game accordingly, including dealing additional cards, calculating scores, determining the winner, and updating the balance.

The code defines a function update_balance that updates the player's balance based on the bet outcome.
The code defines a function update_labels that updates the labels displaying the player's and dealer's hands.
The initial balance is set to 100.

The code creates a tkinter window.
The bet input, labels for the player's and dealer's hands, and balance label are created and positioned in the window.
Buttons for starting the game, hitting, standing, and quitting are created and positioned in the window.
The tkinter main loop is started to handle user interactions with the window and buttons.

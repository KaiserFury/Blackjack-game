Here's a `README.md` file for your Blackjack game:

```markdown
# Blackjack Game

This is a simple terminal-based Blackjack game written in Python. The game follows the classic Blackjack rules, where the goal is to get as close to a score of 21 without going over, while competing against the computer. 

## Features
- Automatically deals two cards to the player and the computer.
- The player can choose to draw additional cards or pass.
- The game calculates the winner based on Blackjack rules:
  - A hand of 21 with exactly two cards is considered a "Blackjack" and automatically wins.
  - If the player or computer exceeds 21, they lose.
  - Aces can be counted as 11 or 1, depending on the situation.
- The game displays both the player's and the computer's cards and scores.
  
## How to Play
1. Run the game, and you will be dealt two cards. The computer will also be dealt two cards.
2. You will see your cards and the first card of the computer.
3. Choose whether to draw another card or pass:
   - Type `"yes"` to draw another card.
   - Type `"no"` to pass.
4. The computer will keep drawing cards until its total score reaches at least 17.
5. After both the player and the computer finish drawing cards, the game will display the final results and declare the winner.

## How to Run

To play the game, follow these steps:

1. Ensure you have Python installed on your system.
2. Download or clone the repository.
3. Run the `blackjack.py` script in your terminal:
   ```bash
   python blackjack.py
   ```

## Dependencies
- The game relies on an ASCII art file (`Art.py`) to display the Blackjack logo at the beginning of each round. Make sure to include this file in your project.

## Functions

### `number_list_adder(list_name)`
This function calculates the total score for the cards in the list. It accounts for Blackjack rules, such as treating an Ace (11) as 1 if the total score exceeds 21.

### `score_compare(score1, score2)`
Compares the player's and computer's scores to determine the result of the game (win, lose, or draw).

### `blackjack()`
Main game logic where the player and the computer are dealt cards, and the winner is determined based on their final scores.

## Example Gameplay
```bash
Your cards: [10, 9], Your total score is 19
Computer's first card: 8
Type 'yes' to get another card, or type 'no' to pass: no

Your final cards: [10, 9], Total score: 19
Computer's final cards: [8, 10], Total score: 18

YOU WON!
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```


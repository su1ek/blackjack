# Blackjack

A console-based implementation of Blackjack card game written in Python using OOP principles.

## Features
- 52 card deck
- Random card shuffling
- Card dealing system
- Player vs Dealer gameplay
- Ace value adjustment
- Blackjack detection
- Dealer AI (he hits until the value of his cards reach at least 17)
- Input validation (you must either hit or stand)
- Can play multiple games in one session

## Technologies
- Python 3
- Object-Oriented Programming

## Future Improvements
- Graphical user interface
- Card images instead of text
- Betting system
- Player statistics

## Project Structure

```text
Card
├── Represents a single playing card

Deck
├── Creates a standard 52-card deck
├── Shuffles the deck
└── Deals cards

Hand
├── Stores cards
├── Calculates hand value
└── Detects Blackjack

Game
├── Controls game flow
├── Handles player decisions
└── Determines the winner
```
## How to Run

Clone the repository:

```bash
git clone https://github.com/su1ek/blackjack.git
```
Run the application
```bash
python main.py
```
## Example Gameplay

```text
******************************
Game 1 of 3
******************************

Your hand
A of ♥
8 of ♣
Value: 19

Dealer's hand
Hidden
K of ♠

Please choose "Hit" or "Stand"
```

## What I Learned

* Object-oriented programming in Python
* Working with multiple classes
* Managing game state
* Implementing Blackjack game rules
* Input validation
* Writing clean and modular code

## Author

**Bartłomiej Sułkowski**

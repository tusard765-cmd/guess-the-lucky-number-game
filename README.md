# Guess the Lucky Number 🎲

A beginner-friendly Python terminal game. The computer picks a random number from **1 to 100**, and you keep guessing until you find it.

## Features

- Random secret number for each game
- Hints for guesses that are too high or too low
- Friendly handling of non-numeric inputs
- Checks that guesses are within 1–100

## Requirements

- Python 3 (no third-party packages)

## Run the game

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python guess_the_number.py
   ```

   On some systems, use `python3` instead of `python`.

## Example

```text
Guess the lucky number between 1 and 100!
Guess the lucky number: hello
Please enter a valid whole number.
Guess the lucky number: 200
Please enter a number between 1 and 100.
Guess the lucky number: 50
Too high, try again.
```

## About

A small practice project for learning Python loops, conditions, input validation, and the `random` module.

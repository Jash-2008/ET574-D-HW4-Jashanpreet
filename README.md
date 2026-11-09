# ET574 Homework 4 – Dice Game Simulator

## Project Description
This project is a Python Dice Game Simulator. It uses two six-sided dice and determines the result based on the total rolled.

## Project Files
- `main.py` – Contains the Die class, DiceGame class, and console menu.
- `test_dicegame.py` – Contains the original instructor tests and three additional test cases.

## How to Run the Program

Run the following command:

```bash
python main.py
```

## How to Run Tests

Run the following command:

```bash
python -m unittest -v
```

## AI Usage

**AI Tool Used:** ChatGPT (GPT-6).

AI was used to help understand the assignment requirements, develop the Python program, identify compatibility issues, and create additional unit tests.

Examples of prompts used:
- Explain the requirements for the Dice Game assignment.
- Help implement the Die and DiceGame classes.
- Suggest additional unit tests for the dice game.
- Help identify and correct Python indentation and compatibility issues.

### Evaluation and Modifications

The suggested code was reviewed against the instructor's starter test file. The Die constructor was adjusted to use the `sides` parameter so it would work with the provided tests.

The additional tests were also reviewed to ensure they checked the expected behavior of the program.

## Test Case Modifications

Three additional test cases were added:

1. `test_play_round_dice_values_within_bounds` – Checks that both dice produce values between 1 and 6.
2. `test_play_round_total_is_sum` – Checks that the total equals the sum of both dice.
3. `test_play_round_result_is_correct` – Checks that the returned result matches the outcome calculated by `evaluate_roll()`.

The original instructor-provided tests were retained.

## Reflection on AI Usage

Using AI helped me understand the assignment requirements and organize the programming tasks. I learned how to create unit tests, check returned values, and identify errors in Python code.

I also learned that AI-generated suggestions must be reviewed and tested to make sure they match the assignment requirements.

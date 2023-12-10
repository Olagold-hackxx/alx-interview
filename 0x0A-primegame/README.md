
```markdown
# Prime Game

## Introduction
This Python project implements a game played by Maria and Ben. They take turns choosing a prime number from a set of consecutive integers starting from 1 up to and including n. The chosen prime number and its multiples are then removed from the set. The player that cannot make a move loses the game. The project includes a function to determine the winner of each game played over multiple rounds.

## Task Description
Create a function `isWinner(x, nums)` where:
- `x` is the number of rounds.
- `nums` is an array of `n` values.
Return: the name of the player that won the most rounds. If the winner cannot be determined, return `None`. The players play optimally, and Maria always goes first.

## Requirements
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable
- You cannot import any packages in this task
- You can assume `n` and `x` will not be larger than 10000

## Example Usage
```python
# main_0.py

#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
```

## Example Explanation
- First round (n=4): Ben wins
- Second round (n=5): Maria wins
- Third round (n=1): Ben wins
Result: Ben has the most wins

## Files Structure
- `0-prime_game.py`: Contains the implementation of the `isWinner` function.
- `main_0.py`: A sample script demonstrating the usage of the function.

## Author
[Aileru Abdulqoyyum]

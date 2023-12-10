```markdown
# Island Perimeter

## Introduction
This Python project includes a function to calculate the perimeter of an island based on a given grid.

## Task Description
Create a function `island_perimeter(grid)` that returns the perimeter of the island described in the grid:
- `grid` is a list of lists of integers:
  - 0 represents water
  - 1 represents land
- Each cell is square, with a side length of 1.
- Cells are connected horizontally/vertically (not diagonally).
- The grid is rectangular, with its width and height not exceeding 100.
- The grid is completely surrounded by water.
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

## Requirements
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7)
- You are not allowed to import any module
- All modules and functions must be documented
- All your files must be executable

## Example Usage
```python
from island_perimeter import island_perimeter

grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

result = island_perimeter(grid)
print(result)  # Output: 12
```

## File Structure
- `0-island_perimeter.py`: Contains the implementation of the `island_perimeter` function.
- `0-main.py`: A sample script demonstrating the usage of the function.

## Author
[Abdulqoyyum Aileru]

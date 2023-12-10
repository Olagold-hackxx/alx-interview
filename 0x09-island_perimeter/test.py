def island_perimeter(grid):
    perimeter = 0

    if not grid:
        return perimeter

    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Count top edge
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Count bottom edge
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Count left edge
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Count right edge
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter

# Test
if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 1],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0]
    ]
    print(island_perimeter(grid))

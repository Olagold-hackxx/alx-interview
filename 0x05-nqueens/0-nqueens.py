import sys

def is_safe(board, row, col):
    # Check if there is a queen in the same column on top
    for i in range(row):
        if board[i] == col:
            return False

        # Check upper diagonal on left side
        if board[i] == col - (row - i):
            return False

        # Check upper diagonal on right side
        if board[i] == col + (row - i):
            return False

    return True

def solve_nqueens(n):
    def solve_util(row, board, result):
        if row == n:
            result.append([i, board[i]] for i in range(n))
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve_util(row + 1, board, result)

    result = []
    solve_util(0, [-1] * n, result)
    return result

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()

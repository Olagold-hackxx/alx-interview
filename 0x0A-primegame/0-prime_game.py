#!/usr/bin/python3
""" Prime Game"""


def isWinner(x, nums):
    """ Prime Game"""
    def is_prime(num):
        """Check if prime"""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def game_winner(n):
        """ Get winner"""
        moves = 0
        while n > 1:
            prime_found = False
            for i in range(2, n + 1):
                if is_prime(i) and n % i == 0:
                    n //= i
                    prime_found = True
                    moves += 1
                    break
            if not prime_found:
                return "Ben"
        return "Maria" if moves % 2 == 0 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = game_winner(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

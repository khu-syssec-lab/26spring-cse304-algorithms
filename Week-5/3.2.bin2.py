import time

def bin2(n: int, k: int) -> int:
    B = [[0] * (k + 1) for _ in range(n + 1)]
    # Complete the code here

    return B[n][k]

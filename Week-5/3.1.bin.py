import time

def bin(n: int, k: int) -> int:
    if k == 0 or n == k:
        return 1
    else:
        # Complete the code here
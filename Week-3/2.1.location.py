from typing import List

def location(low: int, high: int, S: List[int], x: int) -> int:
    if low > high:
        return -1
    else:
        # Complete the code here
from heapq import heappush, heappop
from typing import List, Tuple

class Item:
    def __init__(self, id: int, weight: float, profit: float) -> None:
        self.id: int = id
        self.weight: float = weight
        self.profit: float = profit
        self.profit_per_weight: float = profit / weight
        
def knapsack(n: int, W: float, w: List[float], p: List[float]) -> float:
    heap: List[Tuple[float, Item]] = []
    for i in range(n):
        item: Item = Item(i + 1, w[i], p[i])  # type: ignore
        heappush(heap, (-item.profit_per_weight, item))
    maxprofit: float = 0.0
    total_weight: float = 0.0

    # Complete the code here

    return maxprofit
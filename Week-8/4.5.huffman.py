from heapq import heappush, heappop
from typing import List, Tuple, Optional

class Node:
    def __init__(self, symbol: Optional[str], freq: int) -> None:
        self.symbol: Optional[str] = symbol
        self.freq: int = freq
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None
        
    def preorder(self, path: List[Tuple[Optional[str], int]]) -> None:
        path.append((self.symbol, self.freq))
        if self.left is not None:
            self.left.preorder(path)
        if self.right is not None:
            self.right.preorder(path)

    def inorder(self, path: List[Tuple[Optional[str], int]]) -> None:
        if self.left is not None:
            self.left.inorder(path)
        path.append((self.symbol, self.freq))
        if self.right is not None:
            self.right.inorder(path)

def huffman(n: int, s: List[str], f: List[int]) -> Node:
    heap: List[Tuple[int, Node]] = []
    for i in range(n):
        heappush(heap, (f[i], Node(s[i], f[i])))

    # Complete the code here

    return heappop(heap)[1]
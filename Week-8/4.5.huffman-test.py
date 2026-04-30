import sys
import importlib.util
from typing import List, Tuple, Optional

module_name = "huffman_algo"

test_cases = [
    {"n": 1, "symbols": ["a"], "freqs": [1],
     "expected": [("a", 1)],
     "desc": "single symbol"},
    {"n": 2, "symbols": ["a", "b"], "freqs": [1, 2],
     "expected": [("+", 3), ("a", 1), ("b", 2)],
     "desc": "two symbols"},
    {"n": 3, "symbols": ["a", "b", "c"], "freqs": [1, 2, 4],
     "expected": [("+", 7), ("+", 3), ("a", 1), ("b", 2), ("c", 4)],
     "desc": "three symbols"},
    {"n": 4, "symbols": ["a", "b", "c", "d"], "freqs": [1, 2, 4, 8],
     "expected": [("+", 15), ("+", 7), ("+", 3), ("a", 1), ("b", 2), ("c", 4), ("d", 8)],
     "desc": "four symbols"},
    {"n": 5, "symbols": ["a", "b", "c", "d", "e"], "freqs": [1, 2, 4, 8, 16],
     "expected": [("+", 31), ("+", 15), ("+", 7), ("+", 3), ("a", 1), ("b", 2), ("c", 4), ("d", 8), ("e", 16)],
     "desc": "five symbols"},
    {"n": 6, "symbols": ["a", "b", "c", "d", "e", "f"], "freqs": [1, 2, 4, 8, 16, 32],
     "expected": [("+", 63), ("+", 31), ("+", 15), ("+", 7), ("+", 3), ("a", 1), ("b", 2), ("c", 4), ("d", 8), ("e", 16), ("f", 32)],
     "desc": "six symbols"},
    {"n": 3, "symbols": ["x", "y", "z"], "freqs": [3, 5, 7],
     "expected": [("+", 15), ("z", 7), ("+", 8), ("x", 3), ("y", 5)],
     "desc": "odd frequencies"},
    {"n": 4, "symbols": ["m", "n", "o", "p"], "freqs": [3, 6, 12, 24],
     "expected": [("+", 45), ("+", 21), ("+", 9), ("m", 3), ("n", 6), ("o", 12), ("p", 24)],
     "desc": "mixed frequencies"},
    {"n": 5, "symbols": ["p", "q", "r", "s", "t"], "freqs": [1, 3, 9, 27, 81],
     "expected": [("+", 121), ("+", 40), ("+", 13), ("+", 4), ("p", 1), ("q", 3), ("r", 9), ("s", 27), ("t", 81)],
     "desc": "powers of three"},
    {"n": 3, "symbols": ["alpha", "beta", "gamma"], "freqs": [10, 20, 40],
     "expected": [("+", 70), ("+", 30), ("alpha", 10), ("beta", 20), ("gamma", 40)],
     "desc": "scale factors"},
    {"n": 3, "symbols": ["a", "b", "c"], "freqs": [7, 3, 5],
     "expected": [("+", 15), ("a", 7), ("+", 8), ("b", 3), ("c", 5)],
     "desc": "unsorted frequencies"},
    {"n": 3, "symbols": ["a", "b", "c"], "freqs": [0, 1, 2],
     "expected": [("+", 3), ("+", 1), ("a", 0), ("b", 1), ("c", 2)],
     "desc": "zero frequencies"},
]

def run_test_cases(file_path = '4.5.huffman.py'):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    huffman_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(huffman_module)

    huffman = huffman_module.huffman
    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        n = case["n"]
        symbols = case["symbols"]
        freqs = case["freqs"]
        expected = case["expected"]
        desc = case["desc"]

        print(f"\033[1mExample {i}: {desc}\033[0m")
        root = huffman(n, symbols, freqs)
        path: List[Tuple[Optional[str], int]] = []
        root.preorder(path)
        print(f"Preorder: {path}")

        if path == expected:
            print(f"출력: ✅ Passed")
            passed += 1
        else:
            print(f"출력: ❌ Failed (Expected: {expected}, Got: {path})")
        print(f"{'-'*20}\n")

    print(f"✅ {passed}/{total} 테스트 케이스 통과")
    return passed, total

if __name__ == '__main__':
    run_test_cases()

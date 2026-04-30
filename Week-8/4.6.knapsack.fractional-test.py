import sys
import importlib.util
from typing import List, Tuple

module_name = "knapsack_algo"

# 테스트 케이스 정의: n, 용량 W, 무게 리스트 w, 이익 리스트 p, 예상 최대 이익, 설명

test_cases = [
    {"n": 0, "W": 50, "w": [],               "p": [],           "expected": 0.0,   "desc": "no items"},
    {"n": 3, "W": 0,  "w": [10,20,30],       "p": [60,100,120], "expected": 0.0,   "desc": "zero capacity"},
    {"n": 1, "W": 50, "w": [50],             "p": [100],        "expected": 100.0, "desc": "single exact fit"},
    {"n": 1, "W": 50, "w": [100],            "p": [200],        "expected": 100.0, "desc": "single heavy fractional"},
    {"n": 3, "W": 50, "w": [10,20,30],       "p": [60,100,120], "expected": 240.0, "desc": "multiple fractional"},
    {"n": 3, "W": 50, "w": [30,10,20],       "p": [120,60,100], "expected": 240.0, "desc": "unsorted multiple fractional"},
    {"n": 4, "W": 100,"w": [20,30,50,10],    "p": [40,90,60,20], "expected": 198.0, "desc": "fractional leftover"},
    {"n": 2, "W": 5,  "w": [3,5],            "p": [8,14],       "expected": 14.0,  "desc": "float ratio exact"},
    {"n": 3, "W": 60, "w": [10,20,30],       "p": [60,100,120], "expected": 280.0, "desc": "full capacity exact"},
    {"n": 3, "W": 100,"w": [10,20,30],       "p": [60,100,120], "expected": 280.0, "desc": "capacity greater than total"}
]

def run_test_cases(file_path = '4.6.knapsack.fractional.py'):
    # 모듈 로드
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    ks_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ks_module)

    # 비교를 위한 Item.__lt__ 패치
    ks_module.Item.__lt__ = lambda self, other: (self.profit_per_weight, self.id) < (other.profit_per_weight, other.id)  # type: ignore

    knapsack = ks_module.knapsack
    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        n = case["n"]
        W = case["W"]
        w = case["w"]
        p = case["p"]
        expected = case["expected"]
        desc = case["desc"]

        print(f"\033[1mExample {i}: {desc}\033[0m")
        result = knapsack(n, W, w, p)
        print(f"Max profit: {result}")

        if abs(result - expected) < 1e-6:
            print(f"출력: ✅ Passed")
            passed += 1
        else:
            print(f"출력: ❌ Failed (Expected: {expected}, Got: {result})")
        print(f"{'-'*20}\n")

    print(f"✅ {passed}/{total} 테스트 케이스 통과")
    return passed, total

if __name__ == '__main__':
    run_test_cases()

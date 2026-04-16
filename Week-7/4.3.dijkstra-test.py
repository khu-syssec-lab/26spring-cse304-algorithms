import sys
import importlib.util

module_name = "dijkstra_algo"
INF = float("inf")
test_cases = [
    {
        "n": 2,
        "W": [
            [INF,  INF,  INF],
            [INF,  0,    5],
            [INF,  INF,  0]
        ],
        "expected": [(1, 2, 5)],
        "desc": "Case 1"
    },
    {
        "n": 3,
        "W": [
            [INF,  INF,  INF,  INF],
            [INF,  0,    5,    10],
            [INF,  INF,  0,    2],
            [INF,  INF,  INF,  0]
        ],
        "expected": [(1, 2, 5), (2, 3, 2)],
        "desc": "Case 2"
    },
    {
        "n": 3,
        "W": [
            [INF,  INF,  INF,  INF],
            [INF,  0,    2,    4],
            [INF,  INF,  0,    1],
            [INF,  INF,  INF,  0]
        ],
        "expected": [(1, 2, 2), (2, 3, 1)],
        "desc": "Case 3"
    },
    {
        "n": 4,
        "W": [
            [INF,  INF,  INF,  INF,  INF],
            [INF,  0,    3,    2,    6],
            [INF,  3,    0,    1,    4],
            [INF,  2,    1,    0,    2],
            [INF,  6,    4,    2,    0]
        ],
        "expected": [(1, 3, 2), (1, 2, 3), (3, 4, 2)],
        "desc": "Case 4"
    },
    {
        "n": 5,
        "W": [
            [INF,  INF,  INF,  INF,  INF,  INF],
            [INF,  0,    10,   3,    20,   INF],
            [INF,  INF,  0,    INF,  2,    11],
            [INF,  5,    0,    2,    15,   INF],
            [INF,  INF,  INF,  INF,  0,    3],
            [INF,  INF,  INF,  INF,  INF,  0]
        ],
        "expected": [(1, 3, 3), (3, 2, 0), (2, 4, 2), (4, 5, 3)],
        "desc": "Case 5"
    },
    {
        "n": 6,
        "W": [
            [INF,  INF,  INF,  INF,  INF,  INF,  INF],
            [INF,  0,    7,    9,    INF,  INF,  14],
            [INF,  7,    0,    10,   15,   INF,  INF],
            [INF,  9,    10,   0,    11,   INF,  2],
            [INF,  INF,  15,   11,   0,    6,    INF],
            [INF,  INF,  INF,  INF,  6,    0,    9],
            [INF,  14,   INF,  2,    INF,  9,    0]
        ],
        "expected": [(1, 2, 7), (1, 3, 9), (3, 6, 2), (3, 4, 11), (6, 5, 9)],
        "desc": "Case 6"
    },
    {
        "n": 4,
        "W": [
            [INF,  INF,  INF,  INF,  INF],
            [INF,  0,    1,    4,    INF],
            [INF,  INF,  0,    2,    6],
            [INF,  INF,  INF,  0,    3],
            [INF,  INF,  INF,  INF,  0]
        ],
        "expected": [(1, 2, 1), (2, 3, 2), (3, 4, 3)],
        "desc": "Case 7"
    },
    {
        "n": 4,
        "W": [
            [INF,  INF,  INF,  INF,  INF],
            [INF,  0,    2,    8,    INF],
            [INF,  INF,  0,    3,    5],
            [INF,  INF,  INF,  0,    1],
            [INF,  INF,  INF,  INF,  0]
        ],
        "expected": [(1, 2, 2), (2, 3, 3), (3, 4, 1)],
        "desc": "Case 8"
    },
    {
        "n": 6,
        "W": [
            [INF,  INF,  INF,  INF,  INF,  INF,  INF],
            [INF,  0,    5,    INF,  10,   INF,  INF],
            [INF,  INF,  0,    3,    INF,  1,    INF],
            [INF,  INF,  INF,  0,    2,    INF,  6],
            [INF,  INF,  INF,  INF,  0,    INF,  1],
            [INF,  INF,  INF,  INF,  INF,  0,    2],
            [INF,  INF,  INF,  INF,  INF,  INF,  0]
        ],
        "expected": [(1, 2, 5), (2, 5, 1), (2, 3, 3), (5, 6, 2), (1, 4, 10)],
        "desc": "Case 9"
    },
    {
        "n": 7,
        "W": [
            [INF,  INF,  INF,  INF,  INF,  INF,  INF,  INF],
            [INF,  0,    2,    3,    INF,  INF,  INF,  INF],
            [INF,  2,    0,    1,    4,    INF,  INF,  INF],
            [INF,  3,    1,    0,    2,    7,    INF,  INF],
            [INF,  INF,  4,    2,    0,    3,    1,    INF],
            [INF,  INF,  INF,  7,    3,    0,    2,    5],
            [INF,  INF,  INF,  INF,  INF,  2,    0,    6],
            [INF,  INF,  INF,  INF,  INF,  INF,  6,    0]
        ],
        "expected": [(1, 2, 2), (1, 3, 3), (3, 4, 2), (4, 6, 1), (4, 5, 3), (6, 7, 6)],
        "desc": "Case 10"
    }
]

def run_test_cases(file_path="4.3.dijkstra.py"):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    dijkstra_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dijkstra_module)

    dijkstra = dijkstra_module.dijkstra
    """ 테스트 실행 및 결과 검증 """
    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        n = case["n"]
        W = case["W"]
        expected = case["expected"]
        desc = case["desc"]

        print(f"\033[1mExample {i}: {desc}\033[0m")
        result = dijkstra(n, W)

        if result == expected:
            print(f"출력: {result} ✅ Passed")
            passed += 1
        else:
            print(f"출력: {result} ❌ Failed (Expected: {expected}, Got: {result})")
        print(f"{'-'*20}\n")
    
    print(f"✅ {passed}/{total} 테스트 케이스 통과")
    return passed, total

if __name__ == "__main__":
    run_test_cases()

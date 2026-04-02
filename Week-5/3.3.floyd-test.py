import sys
import importlib.util

# 동적으로 floyd 모듈 import
module_name = "floyd"

INF = float("inf")

# 테스트 케이스
test_cases = [
    {
        "n": 4,
        "W": [
            [0, 3, INF, 7],
            [8, 0, 2, INF],
            [5, INF, 0, 1],
            [2, INF, INF, 0]
        ],
        "expected": [
            [0, 3, 5, 6],
            [5, 0, 2, 3],
            [3, 6, 0, 1],
            [2, 5, 7, 0]
        ],
        "desc": "4x4 그래프 - 기본적인 최단 경로"
    },
    {
        "n": 3,
        "W": [
            [0, 1, INF],
            [INF, 0, 2],
            [INF, INF, 0]
        ],
        "expected": [
            [0, 1, 3],
            [INF, 0, 2],
            [INF, INF, 0]
        ],
        "desc": "3x3 그래프 - 단순 경로"
    },
    {
        "desc": "5x5 그래프 - 대칭 그래프",
        "n": 5,
        "W": [[0, 2, INF, 1, INF],
              [2, 0, 3, INF, INF],
              [INF, 3, 0, 4, INF],
              [1, INF, 4, 0, 5],
              [INF, INF, INF, 5, 0]],
        "expected": [[0, 2, 5, 1, 6],
                     [2, 0, 3, 3, 8],
                     [5, 3, 0, 4, 9],
                     [1, 3, 4, 0, 5],
                     [6, 8, 9, 5, 0]]
    },
    {
        "n": 3,
        "W": [
            [0, INF, INF],
            [INF, 0, INF],
            [INF, INF, 0]
        ],
        "expected": [
            [0, INF, INF],
            [INF, 0, INF],
            [INF, INF, 0]
        ],
        "desc": "3x3 그래프 - 모든 노드가 연결되지 않음"
    },
    {
        "n": 4,
        "W": [
            [0, 5, INF, 10],
            [INF, 0, 3, INF],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0]
        ],
        "expected": [
            [0, 5, 8, 9],
            [INF, 0, 3, 4],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0]
        ],
        "desc": "4x4 그래프 - 경로 중간 INF 처리"
    },
    {
        "n": 2,
        "W": [
            [0, 10],
            [INF, 0]
        ],
        "expected": [
            [0, 10],
            [INF, 0]
        ],
        "desc": "2x2 그래프 - 작은 그래프"
    },
    {
        "n": 6,
        "W": [
            [0, 2, 5, INF, INF, INF],
            [INF, 0, 7, 1, INF, INF],
            [INF, INF, 0, 3, 8, INF],
            [INF, INF, INF, 0, 2, 3],
            [INF, INF, INF, INF, 0, 1],
            [INF, INF, INF, INF, INF, 0]
        ],
        "expected": [
            [0, 2, 5, 3, 5, 6],
            [INF, 0, 7, 1, 3, 4],
            [INF, INF, 0, 3, 5, 6],
            [INF, INF, INF, 0, 2, 3],
            [INF, INF, INF, INF, 0, 1],
            [INF, INF, INF, INF, INF, 0]
        ],
        "desc": "6x6 그래프 - 긴 연결 경로"
    },
    {
        "n": 3,
        "W": [
            [0, -1, 4],
            [INF, 0, 3],
            [INF, INF, 0]
        ],
        "expected": [
            [0, -1, 2],
            [INF, 0, 3],
            [INF, INF, 0]
        ],
        "desc": "3x3 그래프 - 음수 가중치"
    },
    {
        "n": 5,
        "W": [
            [0, 10, INF, INF, INF],
            [INF, 0, 5, INF, INF],
            [INF, INF, 0, 2, INF],
            [INF, INF, INF, 0, 1],
            [INF, INF, INF, INF, 0]
        ],
        "expected": [
            [0, 10, 15, 17, 18],
            [INF, 0, 5, 7, 8],
            [INF, INF, 0, 2, 3],
            [INF, INF, INF, 0, 1],
            [INF, INF, INF, INF, 0]
        ],
        "desc": "5x5 그래프 - 계단식 경로"
    },
    {
        "n": 3,
        "W": [
            [0, INF, -2],
            [4, 0, 3],
            [INF, INF, 0]
        ],
        "expected": [
            [0, INF, -2],
            [4, 0, 2],
            [INF, INF, 0]
        ],
        "desc": "3x3 그래프 - 음수 경로 테스트"
    }
]


def run_test_cases(file_path="3.3.floyd.py"):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    floyd_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(floyd_module)

    floyd_func = floyd_module.floyd

    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        n, W, expected, desc = case["n"], case["W"], case["expected"], case["desc"]

        print(f"\033[1m Example {i}: {desc} \033[0m")
        print(f"n = {n}, W =")
        for row in W:
            print(row)

        result = floyd_func(n, W)

        if result == expected:
            print(f"출력: ✅ Passed")
            passed += 1
        else:
            print(f"출력: ❌ Failed")
            print("Expected:")
            for row in expected:
                print(row)
            print("Got:")
            for row in result:
                print(row)

        print(f"{'-'*20}\n")

    print(f"✅ {passed}/{total} 테스트 케이스 통과")
    return passed, total



if __name__ == "__main__":
    run_test_cases()

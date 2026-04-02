import importlib.util
import sys

INF = float("inf")
module_name = "floyd2"
test_cases = [
    {
        "n": 5,
        "W": [
            [0, 7, INF, 2, INF],
            [7, 0, 3, INF, 1],
            [INF, 3, 0, 4, INF],
            [2, INF, 4, 0, 5],
            [INF, 1, INF, 5, 0]
        ],
        "expected": [
            [0, 7, 6, 2, 7],
            [7, 0, 3, 6, 1],
            [6, 3, 0, 4, 4],
            [2, 6, 4, 0, 5],
            [7, 1, 4, 5, 0]
        ],
        "expected_paths": [
            {"i": 0, "j": 2, "path": [1]},
            {"i": 0, "j": 4, "path": [1]},
            {"i": 1, "j": 3, "path": [2]},
            {"i": 3, "j": 1, "path": [2]}
        ],
        "desc": "5x5 그래프 - 대칭 연결"
    },
    {
        "n": 4,
        "W": [
            [0, 5, INF, 10],
            [5, 0, 3, INF],
            [INF, 3, 0, 1],
            [10, INF, 1, 0]
        ],
        "expected": [
            [0, 5, 8, 9],
            [5, 0, 3, 4],
            [8, 3, 0, 1],
            [9, 4, 1, 0]
        ],
        "expected_paths": [
            {"i": 0, "j": 2, "path": [1]},
            {"i": 1, "j": 3, "path": [2]},
            {"i": 3, "j": 0, "path": [2, 1]}
        ],
        "desc": "4x4 그래프 - 일부 단절"
    },
    {
        "n": 3,
        "W": [
            [0, 2, INF],
            [2, 0, 3],
            [INF, 3, 0]
        ],
        "expected": [
            [0, 2, 5],
            [2, 0, 3],
            [5, 3, 0]
        ],
        "expected_paths": [
            {"i": 0, "j": 2, "path": [1]},
            {"i": 2, "j": 0, "path": [1]}
        ],
        "desc": "3x3 간단한 그래프"
    },
    {
        "n": 5,
        "W": [
            [0, 4, 1, INF, INF],
            [4, 0, 2, 7, INF],
            [1, 2, 0, 3, 6],
            [INF, 7, 3, 0, 5],
            [INF, INF, 6, 5, 0]
        ],
        "expected": [
            [0, 3, 1, 4, 7],
            [3, 0, 2, 5, 8],
            [1, 2, 0, 3, 6],
            [4, 5, 3, 0, 5],
            [7, 8, 6, 5, 0]
        ],
        "expected_paths": [
            {"i": 0, "j": 1, "path": [2]},
            {"i": 1, "j": 3, "path": [2]},
            {"i": 3, "j": 4, "path": [2]}
        ],
        "desc": "5x5 다양한 경로 포함"
    },
    {
        "n": 4,
        "W": [
            [0, INF, 1, INF],
            [INF, 0, INF, 2],
            [1, INF, 0, 3],
            [INF, 2, 3, 0]
        ],
        "expected": [
            [0, 6, 1, 4],
            [6, 0, 5, 2],
            [1, 5, 0, 3],
            [4, 2, 3, 0]
        ],
        "expected_paths": [
            {"i": 0, "j": 1, "path": [2]},
            {"i": 2, "j": 1, "path": [3]},
            {"i": 3, "j": 0, "path": [2]}
        ],
        "desc": "4x4 그래프 - 다이렉트 경로 부족"
    },
    {
        "n": 4,
        "W": [
            [0, 5, INF, 10],
            [5, 0, 3, INF],
            [INF, 3, 0, 1],
            [10, INF, 1, 0]
        ],
        "expected": [
            [0, 5, 8, 9],
            [5, 0, 3, 4],
            [8, 3, 0, 1],
            [9, 4, 1, 0]
        ],
        "expected_paths": [
            {"i": 0, "j": 2, "path": [1]},
            {"i": 1, "j": 3, "path": [2]}
        ],
        "desc": "4x4 그래프 - 일부 단절"
    },
    {
        "n": 3,
        "W": [
            [0, 2, INF],
            [2, 0, 3],
            [INF, 3, 0]
        ],
        "expected": [
            [0, 2, 5],
            [2, 0, 3],
            [5, 3, 0]
        ],
        "expected_paths": [
            {"i": 0, "j": 2, "path": [1]}
        ],
        "desc": "3x3 간단한 그래프"
    },
    {
        "n": 5,
        "W": [
            [0, 4, 1, INF, INF],
            [4, 0, 2, 7, INF],
            [1, 2, 0, 3, 6],
            [INF, 7, 3, 0, 5],
            [INF, INF, 6, 5, 0]
        ],
        "expected": [
            [0, 3, 1, 4, 7],
            [3, 0, 2, 5, 8],
            [1, 2, 0, 3, 6],
            [4, 5, 3, 0, 5],
            [7, 8, 6, 5, 0]
        ],
        "expected_paths": [
            {"i": 0, "j": 1, "path": [2]},
            {"i": 1, "j": 3, "path": [2]}
        ],
        "desc": "5x5 다양한 경로 포함"
    },
    {
        "n": 3,
        "W": [
            [0, INF, 2],
            [2, 0, 3],
            [INF, 3, 0]
        ],
        "expected": [
            [0, 5, 2],
            [2, 0, 3],
            [5, 3, 0]
        ],
        "expected_paths": [
            {"i": 0, "j": 2, "path": [1]},
            {"i": 2, "j": 0, "path": [1]}
        ],
        "desc": "3x3 간단한 그래프"
    },
    {
        "n": 5,
        "W": [
            [0, 4, INF, 1, INF],
            [4, 0, 2, 7, INF],
            [1, 2, 3, 0, 6],
            [INF, 7, 3, 0, 5],
            [INF, INF, 6, 5, 0]
        ],
        "expected": [
            [0, 4, 4, 1, 6],
            [3, 0, 2, 2, 7],
            [1, 2, 3, 0, 5],
            [4, 5, 3, 0, 5],
            [7, 8, 6, 5, 0]
        ],
        "expected_paths": [
            {"i": 0, "j": 1, "path": [2]},
            {"i": 1, "j": 3, "path": [2]},
            {"i": 3, "j": 4, "path": [2]}
        ],
        "desc": "5x5 다양한 경로 포함"
    }
]

_P = []

def path(i, j):
    k = _P[i][j]
    if k != -1:
        path(i, k)
        print("v" + str(k), end = " ")
        path(k, j)

def run_test_cases(file_path="3.4.floyd2.py"):
    global _P
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    floyd_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(floyd_module)

    floyd_func = floyd_module.floyd2

    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        n, W, expected, desc, path_checks = case["n"], case["W"], case["expected"], case["desc"], case.get("expected_paths", [])

        print(f"\033[1m Example {i}: {desc} \033[0m")
        print(f"n = {n}, W =")
        for row in W:
            print(row)

        result, P = floyd_func(n, W)
        _P = P[:]

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

        # for paths in path_checks:
        #     path(paths["i"], paths["j"])
        print(f"{'-'*20}\n")

    print(f"✅ {passed}/{total} 테스트 케이스 통과")
    return passed, total


if __name__ == "__main__":
    run_test_cases()

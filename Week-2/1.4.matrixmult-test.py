import sys
import importlib.util
import random


# 동적으로 import
module_name = "matrixmult"
file_path = "1.4.matrixmult.py"

# 테스트 케이스 정의
test_cases = [
    {
        "n": 2,
        "A": [[1, 2], [3, 4]],
        "B": [[5, 6], [7, 8]],
        "expected": [[19, 22], [43, 50]],
        "desc": "기본적인 2x2 행렬 곱셈"
    },
    {
        "n": 1,
        "A": [[3]],
        "B": [[7]],
        "expected": [[21]],
        "desc": "1x1 행렬 곱셈"
    },
    {
        "n": 3,
        "A": [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        "B": [[2, 3, 4], [5, 6, 7], [8, 9, 10]],
        "expected": [[2, 3, 4], [5, 6, 7], [8, 9, 10]],
        "desc": "단위 행렬 곱셈"
    },
    {
        "n": 3,
        "A": [[2, -1, 3], [4, 0, -2], [1, 5, -3]],
        "B": [[0, 1, -1], [2, -2, 3], [-3, 4, -2]],
        "expected": [[-11, 16, -11], [6, -4, 0], [19, -21, 20]],
        "desc": "음수 포함 행렬"
    },
    {
        "n": 3,
        "A": [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        "B": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        "expected": [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        "desc": "0 행렬 곱셈"
    },
    {
        "n": 2,
        "A": [[100, 200], [300, 400]],
        "B": [[500, 600], [700, 800]],
        "expected": [[190000, 220000], [430000, 500000]],
        "desc": "큰 수 포함 행렬"
    },
    {
        "n": 3,
        "A": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        "B": [[9, 8, 7], [6, 5, 4], [3, 2, 1]],
        "expected": [[30, 24, 18], [84, 69, 54], [138, 114, 90]],
        "desc": "정방 행렬 곱셈"
    },
    {
        "n": 2,
        "A": [[2, 3], [4, 5]],
        "B": [[0, 0], [0, 0]],
        "expected": [[0, 0], [0, 0]],
        "desc": "0 행렬과 곱셈"
    },
    {
        "n": 3,
        "A": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        "B": [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        "expected": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        "desc": "단위 행렬과 곱셈"
    },
    {
        "n": 3,
        "A": [[3, -1, 2], [0, 4, -2], [-3, 5, 1]],
        "B": [[1, 2, -3], [4, 5, 6], [-1, 0, 2]],
        "expected": [[-3, 1, -11], [18, 20, 20], [16, 19, 41]],
        "desc": "복합 연산 포함 행렬"
    },
    {
        "n": 5,
        "A": [[random.randint(1, 10) for _ in range(5)] for _ in range(5)],
        "B": [[random.randint(1, 10) for _ in range(5)] for _ in range(5)],
        "expected": None,  
        "desc": "랜덤 5x5 행렬 곱셈 (동적 검증)"
    },
    {
        "n": 100,
        "A": [[random.randint(1, 5) for _ in range(100)] for _ in range(100)],
        "B": [[random.randint(1, 5) for _ in range(100)] for _ in range(100)],
        "expected": None, 
        "desc": "100x100 랜덤 행렬 곱셈 (큰 행렬)"
    }
    # ,
    # {
    #     "n": 500,
    #     "A": [[random.randint(1, 5) for _ in range(500)] for _ in range(500)],
    #     "B": [[random.randint(1, 5) for _ in range(500)] for _ in range(500)],
    #     "expected": None,  # 실행 시 직접 계산
    #     "desc": "500x500 랜덤 행렬 곱셈 (더 큰 행렬)"
    # }
]

# ✅ 랜덤 행렬의 expected 값 미리 계산
for case in test_cases:
    if case["expected"] is None:
        n, A, B = case["n"], case["A"], case["B"]
        C = [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        case["expected"] = C


def run_test_cases(file_path=file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    matrixmult_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(matrixmult_module)

    matrixmult = matrixmult_module.matrixmult
    """ 테스트 실행 및 결과 검증 """
    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        n, A, B, expected, desc = case["n"], case["A"], case["B"], case["expected"], case["desc"]
        print(f"\033[1m Example {i}: {desc}\033[0m")
        print(f"A = {A}")
        print(f"B = {B}")
        result = matrixmult(n, A, B)

        # 결과 검증
        if result == expected:
            print(f"출력: {result} ✅ Passed")
            passed += 1
        else:
            print(f"출력: {result} ❌ Failed (Expected: {expected}, Got: {result})")
            break

        print(f"{'-'*20}\n")

    # 최종 테스트 결과 요약
    print(f"✅ {passed}/{total} 테스트 케이스 통과")
    return passed, total

if __name__ == "__main__":
    run_test_cases()

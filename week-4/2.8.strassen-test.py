import sys
import importlib.util

module_name = "strassen"

def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def sequential_matrix(n):
    mat = []
    num = 1
    for i in range(n):
        row = []
        for j in range(n):
            row.append(num)
            num += 1
        mat.append(row)
    return mat

def conventional_multiply(matA, matB):
    n = len(matA)
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matA[i][k] * matB[k][j]
    return result

test_cases = [
    {
        "n": 1,
        "A": [[5]],
        "B": [[3]],
        "expected": [[15]],
        "desc": "1x1 행렬 곱셈"
    },
    {
        "n": 2,
        "A": [[1, 2], [3, 4]],
        "B": [[5, 6], [7, 8]],
        "expected": [[1*5 + 2*7, 1*6 + 2*8],
                     [3*5 + 4*7, 3*6 + 4*8]],  # [[19,22],[43,50]]
        "desc": "2x2 행렬 곱셈"
    },
    {
        "n": 2,
        "A": [[1, 0], [0, 1]],
        "B": [[9, 8], [7, 6]],
        "expected": [[9, 8], [7, 6]],
        "desc": "2x2 항등 행렬과의 곱셈"
    },
    {
        "n": 2,
        "A": [[-1, 2], [3, -4]],
        "B": [[-5, 6], [7, -8]],
        "expected": [[(-1)*(-5) + 2*7, (-1)*6 + 2*(-8)],
                     [3*(-5) + (-4)*7, 3*6 + (-4)*(-8)]],  # 계산: [[19, -22], [-43, 50]]
        "desc": "2x2 음수 포함 행렬 곱셈"
    },
    {
        "n": 4,
        "A": [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ],
        "B": [
            [16, 15, 14, 13],
            [12, 11, 10, 9],
            [8, 7, 6, 5],
            [4, 3, 2, 1]
        ],
        # 미리 계산한 결과:
        # Row0: [80, 70, 60, 50]
        # Row1: [240, 214, 188, 162]
        # Row2: [400, 358, 316, 274]
        # Row3: [560, 502, 444, 386]
        "expected": [
            [80, 70, 60, 50],
            [240, 214, 188, 162],
            [400, 358, 316, 274],
            [560, 502, 444, 386]
        ],
        "desc": "4x4 순차 행렬 곱셈"
    },
    {
        "n": 4,
        "A": [
            [0, 0, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 1, 1, 1]
        ],
        "B": [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ],
        # Row0: [0,0,0,0]
        # Row1: [1+0+9+0, 2+0+10+0, 3+0+11+0, 4+0+12+0] = [10, 12, 14, 16]
        # Row2: [0+5+0+13, 0+6+0+14, 0+7+0+15, 0+8+0+16] = [18, 20, 22, 24]
        # Row3: [1+5+9+13, 2+6+10+14, 3+7+11+15, 4+8+12+16] = [28, 32, 36, 40]
        "expected": [
            [0, 0, 0, 0],
            [10, 12, 14, 16],
            [18, 20, 22, 24],
            [28, 32, 36, 40]
        ],
        "desc": "4x4 0,1 행렬 곱셈"
    },
    {
        "n": 4,
        "A": [
            [2, -1, 0, 3],
            [4, 5, -2, 1],
            [0, 1, 3, 2],
            [3, 0, -1, 4]
        ],
        "B": [
            [1, 0, 2, -1],
            [3, 4, 0, 2],
            [-2, 1, 5, 3],
            [0, -3, 4, 1]
        ],
        # 직접 계산한 결과:
        # Row0: [ -1, -13, 16, -1 ]
        # Row1: [ 23, 15, 2, 1 ]
        # Row2: [ -3, 1, 23, 13 ]
        # Row3: [ 5, -13, 17, -2 ]
        "expected": [
            [-1, -13, 16, -1],
            [23, 15, 2, 1],
            [-3, 1, 23, 13],
            [5, -13, 17, -2]
        ],
        "desc": "4x4 음수 포함 행렬 곱셈"
    },
    {
        "n": 8,
        "A": identity_matrix(8),
        "B": [[(i+1)*(j+2) % 10 for j in range(8)] for i in range(8)],
        # A가 항등 행렬이므로 expected = B
        "expected": None,
        "desc": "8x8 항등 행렬과 임의의 행렬 곱셈 (항등)"
    },
    {
        "n": 8,
        "A": sequential_matrix(8),
        "B": sequential_matrix(8),
        "expected": None,  # 아래에서 conventional_multiply()로 계산
        "desc": "8x8 순차 행렬 곱셈 (A와 B가 동일)"
    },
    {
        "n": 8,
        "A": [
            [-1, 2, -3, 4, -5, 6, -7, 8],
            [8, -7, 6, -5, 4, -3, 2, -1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3, 3, 3, 3],
            [4, 4, 4, 4, 4, 4, 4, 4],
            [5, 5, 5, 5, 5, 5, 5, 5],
            [6, 6, 6, 6, 6, 6, 6, 6]
        ],
        "B": identity_matrix(8),
        # B가 항등 행렬이므로 expected = A
        "expected": None,
        "desc": "8x8 음수 포함 행렬 곱셈 (항등 행렬과의 곱셈)"
    }
]

# Test 8: A가 항등 행렬이므로 expected를 B로 설정
test_cases[7]["expected"] = test_cases[7]["B"]

# Test 9: 8x8 순차 행렬 곱셈 (A와 B가 동일)의 expected 계산
seq8 = sequential_matrix(8)
test_cases[8]["expected"] = conventional_multiply(seq8, seq8)

# Test 10: 8x8 음수 포함 행렬 곱셈 (B가 항등 행렬)이므로 expected = A
test_cases[9]["expected"] = test_cases[9]["A"]


def run_test_cases(file_path='2.8.strassen.py'):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    strassen_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(strassen_module)

    Matrix = strassen_module.Matrix
    strassen = strassen_module.strassen

    """ 테스트 실행 및 결과 검증 """
    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        n = case["n"]
        A_list = case["A"]
        B_list = case["B"]
        desc = case["desc"]

        A = Matrix(A_list)
        B = Matrix(B_list)
        expected = case["expected"]

        # Strassen 알고리즘으로 행렬 곱셈 수행
        result_matrix = strassen(n, A, B).matrix

        print(f"\033[1m Example {i}: {desc}\033[0m")
        print(f"A: {A_list}")
        print(f"B: {B_list}")
        print(f"Computed Result: {result_matrix}")
        print(f"Expected Result: {expected}")

        if result_matrix == expected:
            print(f"출력: {result_matrix} ✅ Passed")
            passed += 1
        else:
            print(f"출력: {result_matrix} ❌ Failed")
        print(f"{'-'*20}\n")

    print(f"✅ {passed}/{total} 테스트 케이스 통과")
    return passed, total


if __name__ == "__main__":
    run_test_cases()

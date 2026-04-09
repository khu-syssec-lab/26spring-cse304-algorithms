import sys
import importlib.util
import time

module_name = "minmatrixmult"

test_cases = [
    {"d": [5, 10, 3], "expected_cost": 150, "desc": "2개 행렬"},
    {"d": [10, 20, 30, 40], "expected_cost": 18000, "desc": "3개 행렬"},
    {"d": [40, 20, 30, 10, 30], "expected_cost": 26000, "desc": "중첩 구조"},
    {"d": [10, 30, 5, 60], "expected_cost": 4500, "desc": "중간 곱셈"},
    {"d": [30, 35, 15, 5, 10, 20, 25], "expected_cost": 15125, "desc": "일반"},
    {"d": [5, 10, 20, 35], "expected_cost": 4500, "desc": "작은 차원"},
    {"d": [10, 100, 5, 50], "expected_cost": 7500, "desc": "큰 값 혼합"},
    {"d": [2, 3, 6, 4, 5], "expected_cost": 124, "desc": "작은 행렬"},
    {"d": [7, 15, 3, 20, 25], "expected_cost": 2340, "desc": "여러 분할"},  
    {"d": [100, 20, 30, 40, 50], "expected_cost": 164000, "desc": "첫 행렬 큼"},  
    {"d": [10, 20, 30, 40, 30], "expected_cost": 30000, "desc": "중간 값 반복"},
    {
    "d": [30, 35, 15, 5, 10, 20, 25, 10, 15, 30, 5, 10, 20, 25, 30, 35, 40, 20, 15, 10, 5],
    "expected_cost": 42375,
    "desc": "20개 행렬"
    }
]

def run_test_cases(file_path='3.6.minmatrixmult.py'):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    minmult = module.minmult
    order = module.order

    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        d = case["d"]
        expected_cost = case["expected_cost"]
        desc = case["desc"]
        n = len(d) - 1

        print(f"\033[1m Example {i}: {desc}\033[0m")
        print(f"d = {d}")

        start_time = time.time()
        result_cost, M, P = minmult(n, d)
        result_order = order(1, n, P)
        elapsed_time = (time.time() - start_time) * 1000

        time_warning = " ⚠️" if elapsed_time > 100 else ""
        print(f"걸린 시간: {elapsed_time:.3f} ms{time_warning}")

        if result_cost == expected_cost:
            print(f"최소 곱셈 횟수: {result_cost} ✅ Passed")
            passed += 1
        else:
            print(f"최소 곱셈 횟수: {result_cost} ❌ Failed (Expected: {expected_cost})")

        print(f"곱셈 순서: {result_order}")

        # print("P[i][j] 행렬 (최적 분할 위치):")
        # for i in range(1, n):
        #     row = []
        #     for j in range(1, n + 1):
        #         if i < j:
        #             row.append(f"{P[i][j]:>3}")
        #         else:
        #             row.append("   ")
        #     print(" ".join(row))

        print(f"{'-'*20}\n")
    
    print(f"✅ {passed}/{total} 테스트 케이스 통과")
    return passed, total

if __name__ == "__main__":
    run_test_cases()

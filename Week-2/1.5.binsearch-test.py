import sys
import importlib.util

# 동적으로 binsearch 모듈 import
module_name = "binsearch"
file_path = "1.5.binsearch.py"

# 테스트 케이스
test_cases = [
    {"S": [1, 3, 5, 7, 9], "x": 5, "expected": 2, "desc": "중간 값 찾기"},
    {"S": [1, 3, 5, 7, 9], "x": 1, "expected": 0, "desc": "첫 번째 값 찾기"},
    {"S": [1, 3, 5, 7, 9], "x": 9, "expected": 4, "desc": "마지막 값 찾기"},
    {"S": [1, 3, 5, 7, 9], "x": 2, "expected": -1, "desc": "없는 값 찾기"},
    {"S": [], "x": 10, "expected": -1, "desc": "빈 배열"},
    {"S": [42], "x": 42, "expected": 0, "desc": "크기 1인 배열 (존재)"},
    {"S": [42], "x": 10, "expected": -1, "desc": "크기 1인 배열 (없음)"},
    {"S": list(range(1, 1000001, 2)), "x": 777777, "expected": 388888, "desc": "100만 개 중 중간 값 찾기"},
    {"S": list(range(1, 1000001, 2)), "x": 1000001, "expected": -1, "desc": "100만 개 중 없는 값"},
    {"S": list(range(1, 1000001, 2)), "x": 1, "expected": 0, "desc": "100만 개 중 첫 번째 값 찾기"}, 
    {"S": list(range(1, 100000001, 2)), "x": 77777777, "expected": 38888888, "desc": "1억 개 중 중간 값 찾기"},
    {"S": list(range(1, 100000001, 2)), "x": 1000000001, "expected": -1, "desc": "1억 개 중 없는 값"},
    {"S": list(range(1, 100000001, 2)), "x": 1, "expected": 0, "desc": "1억 개 중 첫 번째 값 찾기"}
    # , {"S": list(range(1, 1000000001, 2)), "x": 777777777, "expected": 388888888, "desc": "10억 개 중 중간 값 찾기"},
    # {"S": list(range(1, 1000000001, 2)), "x": 1000000001, "expected": -1, "desc": "10억 개 중 없는 값"},
    # {"S": list(range(1, 1000000001, 2)), "x": 1, "expected": 0, "desc": "10억 개 중 첫 번째 값 찾기"}
]

def run_test_cases(file_path=file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    binsearch_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(binsearch_module)

    binsearch = binsearch_module.binsearch
    """ 테스트 실행 및 결과 검증 """
    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        S, x, expected, desc = case["S"], case["x"], case["expected"], case["desc"]

        print(f"\033[1m Example {i}: {desc}\033[0m")
        print(f"S 크기: {len(S)}")
        print(f"x = {x}")

        result = binsearch(len(S), S, x)

        # 결과 검증
        if result == expected:
            print(f"출력: {result} ✅ Passed")
            passed += 1
        else:
            print(f"출력: {result} ❌ Failed (Expected: {expected}, Got: {result})")

        print(f"{'-'*20}\n")

    # 최종 테스트 결과 요약
    print(f"✅ {passed}/{total} 테스트 케이스 통과")
    return passed, total

if __name__ == "__main__":
    run_test_cases()
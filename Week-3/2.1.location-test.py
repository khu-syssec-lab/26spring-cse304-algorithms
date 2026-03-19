import sys
import importlib.util

# 동적으로 location 모듈 import
module_name = "location"
file_path = "2.1.location_answer.py"

# 테스트 케이스
test_cases = [
    # low > high인 경우 (-1 반환)
    {"low": 5, "high": 2, "S": [1, 2, 3, 4, 5], "x": 3, "expected": -1, "desc": "low > high인 경우"},
    
    # 일반적인 이진 탐색
    {"low": 0, "high": 4, "S": [1, 3, 5, 7, 9], "x": 5, "expected": 2, "desc": "중간 값 찾기"},
    {"low": 0, "high": 4, "S": [1, 3, 5, 7, 9], "x": 1, "expected": 0, "desc": "첫 번째 값 찾기"},
    {"low": 0, "high": 4, "S": [1, 3, 5, 7, 9], "x": 9, "expected": 4, "desc": "마지막 값 찾기"},
    
    # 존재하지 않는 값 찾기
    {"low": 0, "high": 4, "S": [1, 3, 5, 7, 9], "x": 2, "expected": -1, "desc": "없는 값 찾기"},
    
    # 빈 배열
    {"low": 0, "high": -1, "S": [], "x": 10, "expected": -1, "desc": "빈 배열"},
    
    # 크기가 1인 배열
    {"low": 0, "high": 0, "S": [42], "x": 42, "expected": 0, "desc": "크기 1인 배열 (존재)"},
    
    # 배열이 클 경우 (성능 테스트)
    {"low": 0, "high": 999999, "S": list(range(1, 2000000, 2)), "x": 777777, "expected": 388888, "desc": "100만 개 중 중간 값 찾기"},
    {"low": 0, "high": 999999, "S": list(range(1, 2000000, 2)), "x": 2000001, "expected": -1, "desc": "100만 개 중 없는 값"},
    
    # 매우 큰 배열 테스트
    {"low": 0, "high": 99999999, "S": list(range(1, 200000000, 2)), "x": 77777777, "expected": 38888888, "desc": "1억 개 중 중간 값 찾기"},
]

def run_test_cases(file_path='2.1.location.py'):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    location_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(location_module)

    location = location_module.location
    """ 테스트 실행 및 결과 검증 """
    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        low, high, S, x, expected, desc = case["low"], case["high"], case["S"], case["x"], case["expected"], case["desc"]

        print(f"\033[1m Example {i}: {desc}\033[0m")
        print(f"S 크기: {len(S)}")
        print(f"x = {x}")

        result = location(low, high, S, x)

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


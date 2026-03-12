import sys
import importlib.util
import time

# 동적으로 fib1 모듈 import
module_name = "fib1"
file_path = "1.6.fib1.py"

# 테스트 케이스 정의
test_cases = [
    {"n": 0, "expected": 0, "desc": "fib(0)"},
    {"n": 1, "expected": 1, "desc": "fib(1)"},
    {"n": 2, "expected": 1, "desc": "fib(2)"},
    {"n": 3, "expected": 2, "desc": "fib(3)"},
    {"n": 5, "expected": 5, "desc": "fib(5)"},
    {"n": 10, "expected": 55, "desc": "fib(10)"},
    {"n": 20, "expected": 6765, "desc": "fib(20)"},
    {"n": 30, "expected": 832040, "desc": "fib(30)"},
    {"n": 31, "expected": 1346269, "desc": "fib(31)"},
    {"n": 32, "expected": 2178309, "desc": "fib(32)"},
    {"n": 33, "expected": 3524578, "desc": "fib(33)"},
    {"n": 34, "expected": 5702887, "desc": "fib(34)"},
    {"n": 35, "expected": 9227465, "desc": "fib(35)"},
    {"n": 36, "expected": 14930352, "desc": "fib(36)"},
    {"n": 37, "expected": 24157817, "desc": "fib(37)"},
    # {"n": 38, "expected": 39088169, "desc": "fib(38)"},
    # {"n": 40, "expected": 102334155, "desc": "fib(40)"},
]

def run_test_cases(file_path=file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    fib1_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fib1_module)

    fib1 = fib1_module.fib1
    """ 테스트 실행 및 결과 검증 (재귀 함수이므로 작은 값만 테스트) """
    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        n, expected, desc = case["n"], case["expected"], case["desc"]

        print(f"\033[1m Example {i}: {desc}\033[0m")
        print(f"n = {n}")

        start_time = time.time()
        result = fib1(n)
        elapsed_time = (time.time() - start_time) * 1000  # ms 변환

        time_warning = " ⚠️" if elapsed_time > 100 else ""
        print(f"걸린 시간: {elapsed_time:.3f} ms{time_warning}")

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
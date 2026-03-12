import sys
import importlib.util
import time

# 동적으로 fib2 모듈 import
module_name = "fib2"
file_path = "1.7.fib2.py"

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
    {"n": 50, "expected": 12586269025, "desc": "fib(50)"},
    {"n": 60, "expected": 1548008755920, "desc": "fib(60)"},
    {"n": 100, "expected": 354224848179261915075, "desc": "fib(100)"},
    {"n": 1000, "expected": None, "desc": "fib(1,000) (대형 테스트)"},
    {"n": 10000, "expected": None, "desc": "fib(10,000) (초대형 테스트)"},
    {"n": 100000, "expected": None, "desc": "fib(100,000) (초대형 테스트)"}
]

def run_test_cases(file_path=file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    fib2_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fib2_module)

    fib2 = fib2_module.fib2
    """ 테스트 실행 및 결과 검증 """
    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        n, expected, desc = case["n"], case["expected"], case["desc"]

        print(f"\033[1m Example {i}: {desc}\033[0m")
        print(f"n = {n}")

        start_time = time.time()
        # 대형 테스트는 실행만 확인
        if expected is None:
            fib2(n)  # 실행 속도만 확인
            print(f"출력: (Computed)")
            passed += 1
            result = "실행 속도만 확인"
        else:
            result = fib2(n)
        elapsed_time = (time.time() - start_time) * 1000  # ms 변환

        # 실행 시간이 100ms 이상이면 경고 표시
        time_warning = " ⚠️" if elapsed_time > 100 else ""
        print(f"걸린 시간: {elapsed_time:.3f} ms{time_warning}")


        # 결과 검증
        if expected is None:
            print(f"출력: {result} Tested")
        elif result == expected:
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
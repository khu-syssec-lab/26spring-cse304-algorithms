import sys
import importlib.util
import time

# 동적으로 bin 모듈 import
module_name = "bin2"

# 테스트 케이스
test_cases = [
    {"n": 1, "k": 1, "expected": 1, "desc": "C(1,1) = 1"},
    {"n": 10, "k": 1, "expected": 10, "desc": "C(10,1) = 10"},
    {"n": 10, "k": 9, "expected": 10, "desc": "C(10,9) = 10"},
    {"n": 20, "k": 5, "expected": 15504, "desc": "C(20,5) = 15504"},
    {"n": 30, "k": 10, "expected": 30045015, "desc": "C(30,10) = 30045015"},
    {"n": 30, "k": 15, "expected": 155117520, "desc": "C(30,15) = 155117520"},
    {"n": 40, "k": 10, "expected": 847660528, "desc": "C(40,10) = 847660528"},
    {"n": 40, "k": 20, "expected": 137846528820, "desc": "C(40,20) = 137846528820"},
    {"n": 50, "k": 25, "expected": 126410606437752, "desc": "C(50,25) = 126410606437752"},
    {"n": 100, "k": 50, "expected": 100891344545564193334812497256, "desc": "C(100,50) - 100891344545564193334812497256"},
]


def run_test_cases(file_path='3.2.bin2.py'):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    bin_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bin_module)

    bin_func = bin_module.bin2
    
    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        n, k, expected, desc = case["n"], case["k"], case["expected"], case["desc"]

        print(f"\033[1m Example {i}: {desc}\033[0m")
        print(f"n = {n}, k = {k}")
        
        start_time = time.time()
        result = bin_func(n, k)
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

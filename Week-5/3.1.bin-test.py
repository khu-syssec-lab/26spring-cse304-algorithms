import sys
import importlib.util
import time

# 동적으로 bin 모듈 import
module_name = "bin"

# 테스트 케이스
test_cases = [
    {"n": 0, "k": 0, "expected": 1, "desc": "C(0,0) = 1"},
    {"n": 5, "k": 0, "expected": 1, "desc": "C(5,0) = 1"},
    {"n": 5, "k": 5, "expected": 1, "desc": "C(5,5) = 1"},
    {"n": 5, "k": 2, "expected": 10, "desc": "C(5,2) = 10"},
    {"n": 6, "k": 3, "expected": 20, "desc": "C(6,3) = 20"},
    {"n": 7, "k": 4, "expected": 35, "desc": "C(7,4) = 35"},
    {"n": 10, "k": 5, "expected": 252, "desc": "C(10,5) = 252"},
    {"n": 15, "k": 7, "expected": 6435, "desc": "C(15,7) = 6435"},
    {"n": 20, "k": 10, "expected": 184756, "desc": "C(20,10) = 184756"},
    {"n": 27, "k": 15, "expected": 17383860, "desc": "C(25,13) = 17383860"},
    #{"n": 30, "k": 10, "expected": NONE, "desc": "C(30,10) = 30045015(성능 테스트)"},
]

def run_test_cases(file_path='3.1.bin.py'):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    bin_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bin_module)

    bin_func = bin_module.bin
    
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
    
    print(f"✅ {passed}/{total} 테스트 케이스 통과")
    return passed, total


if __name__ == "__main__":
    run_test_cases()

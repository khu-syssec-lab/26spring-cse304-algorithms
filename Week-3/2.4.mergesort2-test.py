import sys
import importlib.util

# merge2 테스트 케이스
test_cases_merge2 = [
    {"low": 0, "mid": 2, "high": 5, "S": [1, 3, 5, 2, 4, 6], "expected": [1, 2, 3, 4, 5, 6], "desc": "두 정렬된 부분 배열 병합"},
    {"low": 0, "mid": 2, "high": 5, "S": [10, 20, 30, 5, 15, 25], "expected": [5, 10, 15, 20, 25, 30], "desc": "교차된 정렬 리스트 병합"},
    {"low": 0, "mid": 2, "high": 5, "S": [1, 2, 3, 4, 5, 6], "expected": [1, 2, 3, 4, 5, 6], "desc": "이미 정렬된 경우"},
    {"low": 0, "mid": 1, "high": 3, "S": [4, 5, 1, 2], "expected": [1, 2, 4, 5], "desc": "작은 배열 병합"},
    {"low": 0, "mid": 1, "high": 3, "S": [10, 20, 5, 15], "expected": [5, 10, 15, 20], "desc": "짝수 개 원소 병합"},
    {"low": 0, "mid": 1, "high": 3, "S": [1, 1, 1, 1], "expected": [1, 1, 1, 1], "desc": "모든 요소가 같은 경우"},
    {"low": 0, "mid": 1, "high": 3, "S": [100, 200, 150, 250], "expected": [100, 150, 200, 250], "desc": "큰 값 포함 병합"},
    {"low": 0, "mid": 2, "high": 5, "S": [-5, 0, 5, -10, -1, 3], "expected": [-10, -5, -1, 0, 3, 5], "desc": "음수 포함 병합"},
    {"low": 0, "mid": 4, "high": 9, "S": [5, 10, 15, 20, 25, 1, 2, 3, 4, 30], "expected": [1, 2, 3, 4, 5, 10, 15, 20, 25, 30], "desc": "비대칭 병합"},
    {"low": 0, "mid": 499999, "high": 999999, "S": list(range(0, 1000000, 2)) + list(range(1, 1000000, 2)), "expected": list(range(1000000)), "desc": "100만 개 병합"},
]


# mergesort2 테스트 케이스
test_cases_mergesort2 = [
    {"S": [3, 1, 4, 1, 5, 9, 2], "expected": [1, 1, 2, 3, 4, 5, 9], "desc": "작은 리스트 정렬"},
    {"S": [10, 20, 30, 5, 15, 25], "expected": [5, 10, 15, 20, 25, 30], "desc": "짝수 개 요소 정렬"},
    {"S": [1, 2, 3, 4, 5], "expected": [1, 2, 3, 4, 5], "desc": "이미 정렬된 리스트"},
    {"S": [5, 4, 3, 2, 1], "expected": [1, 2, 3, 4, 5], "desc": "역순 정렬"},
    {"S": [42], "expected": [42], "desc": "한 개짜리 리스트"},
    {"S": [], "expected": [], "desc": "빈 리스트"},
    {"S": [1, 1, 1, 1], "expected": [1, 1, 1, 1], "desc": "모든 요소가 같은 경우"},
    {"S": [10, -10, 5, -5, 0], "expected": [-10, -5, 0, 5, 10], "desc": "음수 포함 리스트"},
    {"S": [1000, 500, 2000, 1500, 3000], "expected": [500, 1000, 1500, 2000, 3000], "desc": "큰 수 포함 리스트"},
    {"S": list(range(1000000, 0, -1)), "expected": list(range(1, 1000001)), "desc": "100만 개 역순 정렬"},
]


def run_merge2_tests(file_path):
    module_name = "merge2"
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    merge2_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(merge2_module)
    
    merge2 = merge2_module.merge2
    passed = 0
    total = len(test_cases_merge2)
    
    for i, case in enumerate(test_cases_merge2, 1):
        S, low, mid, high, expected, desc = case["S"], case["low"], case["mid"], case["high"], case["expected"], case["desc"]
        original = S[:]
        
        print(f"\033[1m Example {i}: {desc}\033[0m")
        merge2(low, mid, high, S)
        
        if S == expected:
            passed += 1
        else:
            print(f"출력: {S} ❌ Failed (Expected: {expected})")
        print(f"{'-'*20}\n")
    
    print(f"✅ {passed}/{total} merge2 테스트 케이스 통과")
    return passed, total

def run_mergesort2_tests(file_path):
    module_name = "mergesort2"
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    mergesort2_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mergesort2_module)
    
    mergesort2 = mergesort2_module.mergesort2
    passed = 0
    total = len(test_cases_mergesort2)
    
    for i, case in enumerate(test_cases_mergesort2, 1):
        S, expected, desc = case["S"], case["expected"], case["desc"]
        original = S[:]
        
        print(f"\033[1m Example {i}: {desc}\033[0m")
        mergesort2(0, len(S) - 1, S)
        
        if S == expected:
            passed += 1
        else:
            print(f"출력: {S} ❌ Failed (Expected: {expected})")
        print(f"{'-'*20}\n")
    
    print(f"✅ {passed}/{total} mergesort2 테스트 케이스 통과")
    return passed, total


def run_test_cases(file_path="2.4.mergesort2.py"):
    passed, total = run_merge2_tests(file_path)
    passed2, total2 = run_mergesort2_tests(file_path)
    return int((passed+passed2)/2), int((total+total2)/2)

if __name__ == "__main__":
    run_test_cases()

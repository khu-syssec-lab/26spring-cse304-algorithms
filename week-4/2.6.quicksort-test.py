import sys
import importlib.util
import random

module_name = "quicksort"

# 테스트 케이스
random_list = [random.randint(0, 1000) for _ in range(10000)]
test_cases = [
    {"S": [], "expected": [], "desc": "빈 배열"},
    {"S": [42], "expected": [42], "desc": "단일 원소 배열"},
    {"S": [1, 2, 3, 4, 5], "expected": [1, 2, 3, 4, 5], "desc": "이미 정렬된 배열"},
    {"S": [5, 4, 3, 2, 1], "expected": [1, 2, 3, 4, 5], "desc": "역순 정렬 배열"},
    {"S": [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
     "expected": sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]),
     "desc": "중복이 포함된 임의의 배열"},
    {"S": random_list,
     "expected": sorted(random_list),
     "desc": "대용량 랜덤 배열 (10,000개 원소)"},
    {"S": [7, 7, 7, 7, 7],
     "expected": [7, 7, 7, 7, 7],
     "desc": "동일 요소 배열"},
    {"S": [2, 1],
     "expected": [1, 2],
     "desc": "두 원소 배열 (정렬 필요)"},
    {"S": [-3, -1, -7, -5],
     "expected": sorted([-3, -1, -7, -5]),
     "desc": "음수 포함 배열"},
    {"S": [0, -1, 5, -3, 2],
     "expected": sorted([0, -1, 5, -3, 2]),
     "desc": "음수와 양수 및 0 포함 배열"},
]

def run_test_cases(file_path='2.6.quicksort.py'):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    qs_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(qs_module)

    quicksort = qs_module.quicksort

    """ 테스트 실행 및 결과 검증 """
    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        # 원본 리스트를 보존하기 위해 copy 사용
        original_S = case["S"]
        S = original_S.copy()
        expected = case["expected"]
        desc = case["desc"]

        print(f"\033[1m Example {i}: {desc}\033[0m")
        print(f"Original S: {original_S}")

        low = 0
        high = len(S) - 1  
        quicksort(low, high, S)

        print(f"Sorted S: {S}")

        if S == expected:
            print(f"출력: {S} ✅ Passed")
            passed += 1
        else:
            print(f"출력: {S} ❌ Failed (Expected: {expected})")
        print(f"{'-'*20}\n")

    print(f"✅ {passed}/{total} 테스트 케이스 통과")
    return passed, total

if __name__ == "__main__":
    run_test_cases()

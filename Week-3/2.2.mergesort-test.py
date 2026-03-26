import sys
import importlib.util

test_cases_merge = [
    {"U": [1, 3, 5], "V": [2, 4, 6], "expected": [1, 2, 3, 4, 5, 6], "desc": "두 정렬된 리스트 병합"},
    {"U": [10, 20, 30], "V": [5, 15, 25], "expected": [5, 10, 15, 20, 25, 30], "desc": "교차된 정렬 리스트 병합"},
    {"U": [1, 2, 3], "V": [], "expected": [1, 2, 3], "desc": "한 리스트가 빈 경우"},
    {"U": [], "V": [4, 5, 6], "expected": [4, 5, 6], "desc": "한 리스트가 빈 경우 (반대)"},
    {"U": [1, 1, 1], "V": [1, 1, 1], "expected": [1, 1, 1, 1, 1, 1], "desc": "동일한 값 병합"},
    {"U": [1, 3, 5, 7], "V": [2, 4, 6, 8], "expected": [1, 2, 3, 4, 5, 6, 7, 8], "desc": "짝수 개 리스트 병합"},
    {"U": [1], "V": [2], "expected": [1, 2], "desc": "한 개씩 병합"},
    {"U": [100, 200, 300], "V": [150, 250, 350], "expected": [100, 150, 200, 250, 300, 350], "desc": "큰 값이 포함된 병합"},
    {"U": [5, 10, 15, 20], "V": [1, 2, 3, 25], "expected": [1, 2, 3, 5, 10, 15, 20, 25], "desc": "비대칭 병합"},
    {"U": list(range(0, 1000000, 2)), "V": list(range(1, 1000000, 2)), "expected": list(range(1000000)), "desc": "100만 개 병합"}
]

test_cases_mergesort = [
    {"S": [3, 1, 4, 1, 5, 9, 2], "expected": [1, 1, 2, 3, 4, 5, 9], "desc": "작은 리스트 정렬"},
    {"S": [10, 20, 30, 5, 15, 25], "expected": [5, 10, 15, 20, 25, 30], "desc": "짝수 개 요소 정렬"},
    {"S": [1, 2, 3, 4, 5], "expected": [1, 2, 3, 4, 5], "desc": "이미 정렬된 리스트"},
    {"S": [5, 4, 3, 2, 1], "expected": [1, 2, 3, 4, 5], "desc": "역순 정렬"},
    {"S": [42], "expected": [42], "desc": "한 개짜리 리스트"},
    {"S": [], "expected": [], "desc": "빈 리스트"},
    {"S": [1, 1, 1, 1], "expected": [1, 1, 1, 1], "desc": "모든 요소가 같은 경우"},
    {"S": [10, -10, 5, -5, 0], "expected": [-10, -5, 0, 5, 10], "desc": "음수 포함 리스트"},
    {"S": [1000, 500, 2000, 1500, 3000], "expected": [500, 1000, 1500, 2000, 3000], "desc": "큰 수 포함 리스트"},
    {"S": list(range(1000000, 0, -1)), "expected": list(range(1, 1000001)), "desc": "100만 개 역순 정렬"}
]


def run_merge_tests(file_path):
    module_name = "merge"
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    merge_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(merge_module)

    merge = merge_module.merge
    """ 'merge' 함수 테스트 실행 및 결과 검증 """
    passed = 0
    total = len(test_cases_merge)

    for i, case in enumerate(test_cases_merge, 1):
        U, V, expected, desc = case["U"], case["V"], case["expected"], case["desc"]
        h, m = len(U), len(V)
        S = [-1] * (h + m)

        print(f"\033[1m Example {i}: {desc}\033[0m")
        #print(f"U = {U}")
        #print(f"V = {V}")

        merge(h, m, U, V, S)

        if S == expected:
            #print(f"출력: {S} ✅ Passed")
            passed += 1
        else:
            print(f"출력: {S} ❌ Failed (Expected: {expected})")

        print(f"{'-'*20}\n")

    print(f"✅ {passed}/{total} merge 테스트 케이스 통과")
    return passed, total


def run_mergesort_tests(file_path):
    module_name = "mergesort"
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    mergesort_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mergesort_module)

    mergesort = mergesort_module.mergesort
    """ 'mergesort' 함수 테스트 실행 및 결과 검증 """
    passed = 0
    total = len(test_cases_mergesort)

    for i, case in enumerate(test_cases_mergesort, 1):
        S, expected, desc = case["S"], case["expected"], case["desc"]
        original = S[:]

        print(f"\033[1m Example {i}: {desc}\033[0m")
        #print(f"입력: {original}")

        mergesort(len(S), S)

        if S == expected:
            #print(f"출력: {S} ✅ Passed")
            passed += 1
        else:
            print(f"출력: {S} ❌ Failed (Expected: {expected})")

        print(f"{'-'*20}\n")

    print(f"✅ {passed}/{total} mergesort 테스트 케이스 통과")
    return passed, total

def run_test_cases(file_path="2.2.mergesort.py"):
    """ 테스트 실행 및 결과 검증 """
    passed, total = run_merge_tests(file_path)
    passed2, total2 = run_mergesort_tests(file_path)
    return int((passed+passed2)/2), int((total+total2)/2)


if __name__ == "__main__":
    run_test_cases()

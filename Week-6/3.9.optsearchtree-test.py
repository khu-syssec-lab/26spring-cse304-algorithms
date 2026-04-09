import importlib.util
import time

module_name = "optsearchtree"

test_cases = [
    {
        "desc": "n = 1, 하나의 키",
        "n": 1,
        "K": [0, 10],
        "p": [0, 5],
        "expected_minavg": 5,
        "expected_R": [
            [0, 0],
            [0, 1],
            [0, 0]
        ]
    },
    {
        "desc": "n = 2, 균등 빈도",
        "n": 2,
        "K": [0, 10, 20],
        "p": [0, 5, 5],
        "expected_minavg": 15,
        "expected_R": [
            [0, 0, 0],
            [0, 1, 1],
            [0, 0, 2],
            [0, 0, 0]
        ]
    },
    {
        "desc": "n = 2, 오른쪽 치우침",
        "n": 2,
        "K": [0, 10, 20],
        "p": [0, 2, 8],
        "expected_minavg": 12,
        "expected_R": [
            [0, 0, 0],
            [0, 1, 2],
            [0, 0, 2],
            [0, 0, 0]
        ]
    },
    {
        "desc": "n = 3, 좌우 비대칭",
        "n": 3,
        "K": [0, 10, 20, 30],
        "p": [0, 3, 1, 6],
        "expected_minavg": 15,
        "expected_R": [
            [0, 0, 0, 0],
            [0, 1, 1, 3],
            [0, 0, 2, 3],
            [0, 0, 0, 3],
            [0, 0, 0, 0]
        ]
    },
    {
        "desc": "n = 3, 균등 분포",
        "n": 3,
        "K": [0, 10, 20, 30],
        "p": [0, 2, 2, 2],
        "expected_minavg": 10,
        "expected_R": [
            [0, 0, 0, 0],
            [0, 1, 1, 2],
            [0, 0, 2, 2],
            [0, 0, 0, 3],
            [0, 0, 0, 0]
        ]
    },
    {
        "desc": "n = 4, 예제와 동일",
        "n": 4,
        "K": [0, 10, 20, 30, 40],
        "p": [0, 3, 3, 1, 1],
        "expected_minavg": 14,
        "expected_R": [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 2, 2],
            [0, 0, 2, 2, 2],
            [0, 0, 0, 3, 3],
            [0, 0, 0, 0, 4],
            [0, 0, 0, 0, 0]
        ]
    },
    {
        "desc": "n = 4, 오른쪽으로 증가 빈도",
        "n": 4,
        "K": [0, 10, 20, 30, 40],
        "p": [0, 1, 2, 3, 4],
        "expected_minavg": 18,
        "expected_R": [
            [0, 0, 0, 0, 0],
            [0, 1, 2, 2, 3],
            [0, 0, 2, 3, 3],
            [0, 0, 0, 3, 4],
            [0, 0, 0, 0, 4],
            [0, 0, 0, 0, 0]
        ]
    },
    {
        "desc": "n = 5, 중앙 집중 빈도",
        "n": 5,
        "K": [0, 10, 20, 30, 40, 50],
        "p": [0, 1, 10, 10, 10, 1],
        "expected_minavg": 56,
        "expected_R": [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 2, 2, 3, 3],
            [0, 0, 2, 2, 3, 3],
            [0, 0, 0, 3, 3, 4],
            [0, 0, 0, 0, 4, 4],
            [0, 0, 0, 0, 0, 5],
            [0, 0, 0, 0, 0, 0]
        ]
    },
    {
        "desc": "n = 5, 균등",
        "n": 5,
        "K": [0, 10, 20, 30, 40, 50],
        "p": [0, 2, 2, 2, 2, 2],
        "expected_minavg": 22,
        "expected_R": [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 2, 2, 2],
            [0, 0, 2, 2, 3, 3],
            [0, 0, 0, 3, 3, 4],
            [0, 0, 0, 0, 4, 4],
            [0, 0, 0, 0, 0, 5],
            [0, 0, 0, 0, 0, 0]
        ]
    },
    {
        "desc": "n = 6, 중간에 무거운 키",
        "n": 6,
        "K": [0, 5, 10, 15, 20, 25, 30],
        "p": [0, 1, 1, 10, 1, 1, 1],
        "expected_minavg": 23,
        "expected_R": [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 3, 3, 3, 3],
            [0, 0, 2, 3, 3, 3, 3],
            [0, 0, 0, 3, 3, 3, 3],
            [0, 0, 0, 0, 4, 4, 5],
            [0, 0, 0, 0, 0, 5, 5],
            [0, 0, 0, 0, 0, 0, 6],
            [0, 0, 0, 0, 0, 0, 0]
        ]
    },
    {
        "desc": "n = 6, 왼쪽 치우침",
        "n": 6,
        "K": [0, 1, 2, 3, 4, 5, 6],
        "p": [0, 6, 5, 4, 3, 2, 1],
        "expected_minavg": 45,
        "expected_R": [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 2, 2, 2, 2],
            [0, 0, 2, 2, 3, 3, 3],
            [0, 0, 0, 3, 3, 4, 4],
            [0, 0, 0, 0, 4, 4, 4],
            [0, 0, 0, 0, 0, 5, 5],
            [0, 0, 0, 0, 0, 0, 6],
            [0, 0, 0, 0, 0, 0, 0]
        ]
    },
    {
        "desc": "n = 7, 균등",
        "n": 7,
        "K": [0, 1, 2, 3, 4, 5, 6, 7],
        "p": [0, 1, 1, 1, 1, 1, 1, 1],
        "expected_minavg": 17,
        "expected_R": [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 2, 2, 2, 3, 4],
            [0, 0, 2, 2, 3, 3, 3, 4],
            [0, 0, 0, 3, 3, 4, 4, 4],
            [0, 0, 0, 0, 4, 4, 5, 5],
            [0, 0, 0, 0, 0, 5, 5, 6],
            [0, 0, 0, 0, 0, 0, 6, 6],
            [0, 0, 0, 0, 0, 0, 0, 7],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
    }
]

def run_test_cases(file_path='3.9.optsearchtree.py'):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    opt_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(opt_module)

    optsearchtree = opt_module.optsearchtree
    tree = opt_module.tree

    passed = 0
    total = len(test_cases)

    for idx, case in enumerate(test_cases, 1):
        print(f"\033[1mExample {idx}: {case['desc']}\033[0m")
        n = case["n"]
        p = case["p"]
        K = case["K"]
        expected_minavg = case["expected_minavg"]
        expected_R = case["expected_R"]

        start_time = time.time()
        minavg, _, R = optsearchtree(n, p)
        elapsed = (time.time() - start_time) * 1000

        # 트리 구성
        root = tree(1, n, K, R)

        print(f"걸린 시간: {elapsed:.3f} ms {'⚠️' if elapsed > 100 else ''}")
        print(f"minavg: {minavg} (expected: {expected_minavg})")

        minavg_pass = minavg == expected_minavg
        R_pass = all(R[i][j] == expected_R[i][j] for i in range(n + 2) for j in range(n + 1))

        if minavg_pass and R_pass:
            print("✅ Passed")
            passed += 1
        else:
            if not minavg_pass:
                print(f"❌ minavg mismatch: got {minavg}, expected {expected_minavg}")
            if not R_pass:
                print("❌ R matrix mismatch:")
                print("Returned R:")
                for i in range(1, n + 2):
                    print(R[i][i - 1:n + 1])
                print("Expected R:")
                for i in range(1, n + 2):
                    print(expected_R[i][i - 1:n + 1])


        print("-" * 20)

    print(f"\n✅ {passed}/{total} 테스트 케이스 통과")
    return passed, total

if __name__ == "__main__":
    run_test_cases()

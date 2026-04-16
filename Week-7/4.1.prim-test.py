import sys
import importlib.util

INF = float("inf")
module_name = "prim_algo"

test_cases = [
    {
        "n": 2,
        "W": [
            [INF,    INF,    INF],
            [INF,    0,      5],
            [INF,    5,      0]
        ],
        "expected": 5,
        "desc": "단순 2 노드 그래프 (한 간선, 가중치 5)"
    },
    {
        "n": 3,
        "W": [
            [INF,    INF,    INF,    INF],
            [INF,    0,      1,      3],
            [INF,    1,      0,      2],
            [INF,    3,      2,      0]
        ],
        "expected": 3,  # MST: (1,2)=1, (2,3)=2
        "desc": "3 노드 완전 그래프, MST 총 가중치 3 (1+2)"
    },
    {
        "n": 4,
        "W": [
            [INF,    INF,    INF,    INF,    INF],
            [INF,    0,      1,      2,      1],
            [INF,    1,      0,      1,      2],
            [INF,    2,      1,      0,      1],
            [INF,    1,      2,      1,      0]
        ],
        "expected": 3,  # MST: 예를 들어 (1,2)=1, (2,3)=1, (3,4)=1
        "desc": "4 노드 사각형 그래프, MST 총 가중치 3"
    },
    {
        "n": 5,
        "W": [
            [INF,    INF,    INF,    INF,    INF,    INF],
            [INF,    0,      1,      1,      1,      1],
            [INF,    1,      0,      INF,    INF,    INF],
            [INF,    1,      INF,    0,      INF,    INF],
            [INF,    1,      INF,    INF,    0,      INF],
            [INF,    1,      INF,    INF,    INF,    0]
        ],
        "expected": 4,  # MST: 1번에서 모든 노드로 이어지는 스타형 트리, 총 가중치 1*4=4
        "desc": "5 노드 스타형 그래프 (중심 1번), MST 총 가중치 4"
    },
    {
        "n": 5,
        "W": [
            [INF,    INF,    INF,    INF,    INF,    INF],
            [INF,    0,      2,      INF,    INF,    INF],
            [INF,    2,      0,      3,      INF,    INF],
            [INF,    INF,    3,      0,      4,      INF],
            [INF,    INF,    INF,    4,      0,      5],
            [INF,    INF,    INF,    INF,    5,      0]
        ],
        "expected": 14, # MST: 체인 형태로 (1,2)=2, (2,3)=3, (3,4)=4, (4,5)=5 → 총 14
        "desc": "5 노드 선형(체인) 그래프, MST 총 가중치 14"
    },
    {
        "n": 6,
        "W": [
            [INF,    INF,    INF,    INF,    INF,    INF,    INF],
            [INF,    0,      3,      1,      6,      INF,    INF],
            [INF,    3,      0,      5,      2,      4,      INF],
            [INF,    1,      5,      0,      4,      6,      2],
            [INF,    6,      2,      4,      0,      2,      1],
            [INF,    INF,    4,      6,      2,      0,      3],
            [INF,    INF,    INF,    2,      1,      3,      0]
        ],
        "expected": 8,  # MST 예: (1,3)=1, (3,? 등) → 총 8가 되어야 함 (계산에 주의)
        "desc": "6 노드 그래프, 다양한 가중치, MST 총 가중치 8"
    },
    {
        "n": 4,
        "W": [
            [INF,    INF,    INF,    INF,    INF],
            [INF,    0,      1,      1,      1],
            [INF,    1,      0,      1,      1],
            [INF,    1,      1,      0,      1],
            [INF,    1,      1,      1,      0]
        ],
        "expected": 3,  # MST: (1,2)=1, (1,3)=1, (1,4)=1 또는 다른 조합 → 총 3
        "desc": "4 노드 완전 그래프 (모든 간선 가중치 1), MST 총 가중치 3"
    },
    {
        "n": 4,
        "W": [
            [INF,    INF,    INF,    INF,    INF],
            [INF,    0,      2,      5,      INF],
            [INF,    2,      0,      3,      1],
            [INF,    5,      3,      0,      8],
            [INF,    INF,    1,      8,      0]
        ],
        "expected": 6,  # MST: 예를 들어 (1,2)=2, (2,4)=1, (2,3)=3 → 총 6
        "desc": "4 노드 그래프, 일부 간선 없음, MST 총 가중치 6"
    },
    {
        "n": 6,
        "W": [
            [INF,    INF,    INF,    INF,    INF,    INF,    INF],
            [INF,    0,      2,      INF,    INF,    INF,    2],
            [INF,    2,      0,      2,      1,      INF,    INF],
            [INF,    INF,    2,      0,      2,      INF,    INF],
            [INF,    INF,    1,      2,      0,      2,      INF],
            [INF,    INF,    INF,    INF,    2,      0,      2],
            [INF,    2,      INF,    INF,    INF,    2,      0]
        ],
        "expected": 9,  # MST: (1,2)=2, (2,5)=1, (2,3)=2, (3,4)=2, (1,6)=2 → 총 9
        "desc": "6 노드 사이클 + 추가 간선, MST 총 가중치 9"
    },
    {
        "n": 7,
        "W": [
            [INF,    INF,    INF,    INF,    INF,    INF,    INF,    INF],
            [INF,    0,      2,      3,      4,      5,      6,      7],
            [INF,    2,      0,      1,      8,      9,      10,     11],
            [INF,    3,      1,      0,      12,     13,     14,     15],
            [INF,    4,      8,      12,     0,      16,     17,     18],
            [INF,    5,      9,      13,     16,     0,      19,     20],
            [INF,    6,      10,     14,     17,     19,     0,      21],
            [INF,    7,      11,     15,     18,     20,     21,     0]
        ],
        "expected": 25, # MST: (1,2)=2, (2,3)=1, (1,4)=4, (1,5)=5, (1,6)=6, (1,7)=7 → 총 25
        "desc": "7 노드 완전 그래프, MST 총 가중치 25"
    }
]

def run_test_cases(file_path='4.1.prim.py'):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    prim_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prim_module)

    prim = prim_module.prim
    """ 테스트 실행 및 결과 검증 """
    passed = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases, 1):
        n = case["n"]
        W = case["W"]
        expected = case["expected"]
        desc = case["desc"]

        print(f"\033[1mExample {i}: {desc}\033[0m")
        result = prim(n, W)
        total_weight = sum(edge[2] for edge in result)
        print(f"MST Total Weight: {total_weight}")

        if total_weight == expected:
            print(f"출력: {result} ✅ Passed")
            passed += 1
        else:
            print(f"출력: {result} ❌ Failed (Expected: {expected}, Got: {result})")
        print(f"{'-'*20}\n")
    
    print(f"✅ {passed}/{total} 테스트 케이스 통과")
    return passed, total

if __name__ == "__main__":
    run_test_cases()

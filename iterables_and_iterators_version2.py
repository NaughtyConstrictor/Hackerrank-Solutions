# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import comb
from collections import Counter

def probability(N, K, count_a):
    if K > N:
        return 0
    if count_a == 0:
        return 0
    upper = (K if count_a > K else count_a) + 1
    return sum(
        comb(count_a, i) * comb(N - count_a, K - i)
        for i in range(1,  upper)
    ) / comb(N, K)

if __name__ == "__main__":
    N = int(input())
    letters = input().strip().split()
    count_a = Counter(letters)["a"]
    K = int(input())
    print(round(probability(N, K, count_a), 3))

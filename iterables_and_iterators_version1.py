# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

if __name__ == "__main__":
    N = int(input())
    letters = input().strip().split()
    K = int(input())
    i = 0
    j = 0
    for combination in itertools.combinations(letters, K):
        if "a" in combination:
            i += 1
        j += 1
    print(round(i / j, 3))

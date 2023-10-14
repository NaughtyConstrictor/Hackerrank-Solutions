# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

if __name__ == "__main__":
    s = input().strip()
    for group_key, group in groupby(s):
        print(f"({len(list(group))}, {group_key})", end=" ")

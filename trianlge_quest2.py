for level in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(sum(map(lambda x: x * 10**(level - x), range(1, level + 1)))*(10**(level - 1))+ sum(map(lambda x: x * 10**(x - 1), range(level - 1, 0, -1))))

import math
import os
import random
import re
import sys

def transpose(matrix):
    return list(zip(*matrix))

def flatten(matrix):
    return [
            element 
            for row in matrix
            for element in row
    ]


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
message = "".join(flatten(transpose(matrix)))
message = re.sub(r"(\w)[!@#$%& ]+(\w)", r"\1 \2", message)
print(message)

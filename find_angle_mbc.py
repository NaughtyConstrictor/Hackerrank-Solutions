# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import atan, degrees
if __name__ == "__main__":
    ab, bc = [float(input().strip()) for _ in range(2)]
    print(f"{round(degrees(atan(ab / bc)))}{chr(176)}")
    

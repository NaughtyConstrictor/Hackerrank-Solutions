# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def check_card_num(card_num):
    return re.match(
    r"^[456]\d{15}",
    card_num
    )

def check_consecutive_digits(card_num, n=4):
    if len(card_num) < n:
        return False
    digits = set(card_num[:n])
    if len(digits) == 1:
        return True
    return check_consecutive_digits(card_num[1:])

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        card_num = input().strip()
        if len(card_num) < 16 or len(card_num) > 19:
            print("Invalid")
        elif len(card_num) == 16:
            if check_card_num(card_num) and not check_consecutive_digits(card_num):
                print("Valid")
            else:
                print("Invalid")
        else:
            sep = set(card_num[i] for i in range(4, 15, 5))
            if sep != {'-'}:
                print("Invalid")
            else:
                card_num = "".join(
                    (card_num[0:4], 
                    card_num[5:9], 
                    card_num[10:14],
                    card_num[15:19]))
                if check_card_num(card_num) and not check_consecutive_digits(card_num):
                    print("Valid")
                else:
                    print("Invalid")

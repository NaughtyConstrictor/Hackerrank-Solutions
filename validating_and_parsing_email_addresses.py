from re import match
import email.utils

def check_address(address):
    return match(
    r"^[a-zA-Z][\w\-\.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$", 
    address
    )

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        name, address = email.utils.parseaddr(input())
        if check_address(address):
            print(email.utils.formataddr((name, address)))

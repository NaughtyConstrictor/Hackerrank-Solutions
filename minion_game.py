def minion_game(string):
    # your code goes here
    stuart = 0
    kevin = 0
    len_string = len(string)
    for index, char in enumerate(string):
        if char in "AEIOU":
            kevin += (len_string - index)
        else:
            stuart += (len_string - index)
    if stuart > kevin:
        print(f"Stuart {stuart}")
    elif kevin > stuart:
        print(f"Kevin {kevin}")
    else:
        print("Draw")
        
        

if __name__ == '__main__':
    s = input()
    minion_game(s)
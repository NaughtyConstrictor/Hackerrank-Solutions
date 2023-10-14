def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        t = string[i:i+k]
        u = []
        char_set = set()
        for char in t:
            if char not in char_set:
                u.append(char)
            char_set.add(char)
        print("".join(u))


# def merge_the_tools(string, k):
#     # your code goes here
#     for i in range(0, len(string), k):
#         t = string[i:i+k]
#         u = ""
#         for char in t:
#             if char not in u:
#                 u += char
#         print(u)


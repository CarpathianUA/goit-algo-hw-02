from collections import deque


def palindrome_detector(string: str):
    q = deque()

    for char in string.strip().lower().replace(" ", ""):
        q.append(char)

    if not len(q) or len(q) == 1:
        return "String is empty or contains only one character!"

    while len(q) > 1:
        if q.popleft() != q.pop():
            return "Not a palindrome!"

    return "It's a palindrome!"


print(palindrome_detector("race a car"))
print(palindrome_detector("race  car    "))
print(palindrome_detector("not a palindrome"))
print(palindrome_detector(" "))
print(palindrome_detector("o_0"))

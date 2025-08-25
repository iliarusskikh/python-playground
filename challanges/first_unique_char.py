from collections import Counter

def first_unique_char(s):
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None
    
print(first_unique_char("swiss"))

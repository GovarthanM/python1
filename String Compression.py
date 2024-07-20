from typing import List

def compress(chars: List[str]) -> int:
    write = read = 0
    while read < len(chars):
        char = chars[read]
        count = 0
        while read < len(chars) and chars[read] == char:
            read += 1
            count += 1
        chars[write] = char
        write += 1
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
    return write

chars = ["a", "a", "b", "b", "c", "c", "c"]
new_length = compress(chars)
print(new_length)
print(chars[:new_length])
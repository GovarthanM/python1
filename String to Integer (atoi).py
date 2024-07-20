def myAtoi(s: str) -> int:
    import re
    match = re.match(r'^\s*([+-]?\d+)', s)
    if not match:
        return 0
    result = int(match.group(1))
    int_min, int_max = -2**31, 2**31 - 1
    return max(min(result, int_max), int_min)

print(myAtoi("   -42"))
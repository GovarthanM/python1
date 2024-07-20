import re

for _ in range(int(input())):
    print("YES" if re.match(r'^[789]\d{9}$', input()) else "NO")

# Input : 1 
#         7394682671

# Output : YES

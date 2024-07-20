import re

for _ in range(int(input())):
    uid = input().strip()
    if (len(uid) == 10 and
        re.match(r'^[a-zA-Z0-9]+$', uid) and
        len(re.findall(r'[A-Z]', uid)) >= 2 and
        len(re.findall(r'\d', uid)) >= 3 and
        not re.search(r'(.)\1', uid)):
        print("Valid")
    else:
        print("Invalid")

# Input : 1
#         ASDFG12345
 
# Output : Valid    

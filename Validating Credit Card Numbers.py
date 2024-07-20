import re

for _ in range(int(input())):
    card = input().strip()
    if (re.match(r'^[456]\d{3}-?\d{4}-?\d{4}-?\d{4}$', card) and
        not re.search(r'(\d)\1{3,}', card.replace('-', ''))):
        print("Valid")
    else:
        print("Invalid")

# Input : 1
#         6874894561894984

# output : Valid

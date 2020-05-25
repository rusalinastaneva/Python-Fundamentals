import re
n = int(input())

for i in range(n):
    text = input()
    pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"
    match = re.match(pattern, text)

    if match is None:
        print("Invalid barcode")
        continue

    valid_barcode = match.group(1)
    digits = ""

    for ch in valid_barcode:
        if ch.isdigit():
            digits += ch

    if digits == "":
        print(f'Product group: 00')
    else:
        print(f'Product group: {digits}')

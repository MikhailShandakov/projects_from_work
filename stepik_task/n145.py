dcts = ({}, {})
for d in dcts:
    for c in input().lower():
        d[c] = d.get(c, 0) + 1

print(('NO', 'YES')[dcts[0] == dcts[1]])


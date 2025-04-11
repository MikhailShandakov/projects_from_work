s = input()

first_h = s.find("h")

last_h = s.rfind("h")

print(s[:first_h + 1], end='')

print(s[last_h - 1 : first_h : -1], end='')

print(s[last_h:], end='')
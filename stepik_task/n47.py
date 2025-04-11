t1, t2, t3 = input(), input(), input()

max_len = max(len(t1), len(t2), len(t3))

min_len = min(len(t1), len(t2), len(t3))

s = (t1, t2, t3)

print(max_len)
print(min_len)
print(*s)
print(s[0])

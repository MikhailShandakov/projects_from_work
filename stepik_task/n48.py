t1, t2, t3 = input(), input(), input()

for i in [t1, t2, t3]:
    if len(i) == min(len(t1), len(t2), len(t3)):
        print(i)
for i in [t1, t2, t3]:
    if len(i) == max(len(t1), len(t2), len(t3)):
        print(i)

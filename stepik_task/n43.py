n1, n2, n3 = map(int, input())

for i in [n1, n2, n3]:
    if i == max(n1, n2, n3) - min(n1, n2, n3):
        print("Интересно")
        break
else:
    print("не")

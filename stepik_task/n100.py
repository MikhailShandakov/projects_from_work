s = input().upper()

A = ["Аденин:", s.count("А")]
G = ["Гуанин:", s.count("Г")]
C = ["Цитозин:", s.count("Ц")]
T = ["Тимин:", s.count("Т")]

print(*A)
print(*G)
print(*C)
print(*T)
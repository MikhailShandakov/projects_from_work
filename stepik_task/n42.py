a, b, c = int(input()), int(input()), int(input())

print(max(a, b, c))
print(a if a != min(a, b, c)) #and a != max(a, b, c))
#print(b if b != min(a, b, c) and max(a, b, c))
#print(c if c != min(a, b, c) and max(a, b, c))
print(min(a, b, c))

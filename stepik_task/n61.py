m, n = int(input()), int(input())

set_mn = {*range(m, n+1), *range(n, m+1)}

print(*sorted(set_mn, reverse=m>n))

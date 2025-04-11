m, n = int(input()), int(input())

k = abs(m-n)

k_list = [m+x for x in range(k+1)]

k2_list = [m+(-1)*x for x in range(k+1)]





print(k_list if any(n==i in k_list for i in k_list))
print(k2_list if any(n==i in k2_list for i in k2_list))

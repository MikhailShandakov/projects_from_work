n = int(input())

k = n%2

n_new = n - k


res = n*k + ((1+n_new)*n_new/2)

print(res)

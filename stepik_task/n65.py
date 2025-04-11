from random import randrange as r

beg = 1990

end = 2024


random_year = r(beg, end)

random_list = [r(beg, end) for i in range(10)]

random_set = set(random_list)

proof = random_year in random_set

print("Это случилось в", random_year, "году")

print("Похожее было и в", random_set, "годах.", end = " ")

print('"-it is '+str(proof)+'"')

#set сотирует список в некоторых случаях, но достоверно не выясненно когда именно
#Точно понятно что set может сортировать отрицательный range(x,y,-1), может пригодиться




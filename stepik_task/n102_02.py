YRB = "желтый красный синий".split()

res = [["желтый", "оранжевый", "зеленый"],
       ["оранжевый", "красный", "фиолетовый"],
       ["зеленый", "фиолетовый", "синий"]]

answer = "ошибка цвета"

colors = [YRB.index(m) for _ in range(2) if (m := input()) in YRB]

if len(colors) == 2:
    answer = res[colors[0]][colors[1]]
    
print(answer)
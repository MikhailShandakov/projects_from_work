color = input() + input()

if color.count("красный") + color.count("синий") + color.count("желтый") != 2:
    print("ошибка цвета")

elif "красный" in color:
    
    if "синий" in color:
        print("фиолетовый")
    elif "желтый" in color:
        print("оранжевый")
    elif "красныйкрасный" in color:
        print("красный")
        
elif "синий" in color:
    
    if "желтый" in color:
        print("зеленый")
    elif "синийсиний" in color:
        print("синий")
        
else:
    print("желтый")

        
        

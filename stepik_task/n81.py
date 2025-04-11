#x^2+y^2+z^2=19451945

import math

z_max = math.ceil(math.sqrt(19451945))

total = 0

first_list = []

my_list = []

last_list = []

for i in range(19451946):
    if math.sqrt(i) % 1 == 0:
        my_list.append(i)
        
for i in my_list:
    if i * 3 >= 19451945:
        first_list.append(my_list[:my_list.index(i)])
        last_list.append(my_list[my_list.index(i):])
        
        
        
for x2 in my_list:
    for y2 in my_list:
        for z2 in my_list:
            if x2 + y2 + z2 == 19451945:
                print("x =", math.sqrt(x2), "y =", math.sqrt(y2), "z =", math.sqrt(z2),)
                total += 1
                
print(total)
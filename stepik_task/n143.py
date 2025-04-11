bord = [["."] * 8 for _ in range(8)]
row = ["8", "7", "6", "5", "4", "3", "2", "1"]
col = ["a", "b", "c", "d", "e", "f", "g", "h"]

position = input()

ind_row = row.index(position[1])
ind_col = col.index(position[0])


for i in range(8):
    x = abs(ind_row - i)
    for j in range(8):
        y = abs(ind_col - j)
        if (x == y or
            i == ind_row or
            j == ind_col):
            
            bord[i][j] = "*"
            
        if i == ind_row and j == ind_col:
            bord[i][j] = "Q"
            
        print(bord[i][j], end=" ")
    print()
        
            
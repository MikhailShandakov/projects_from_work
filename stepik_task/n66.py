month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

month_enume = enumerate(month, 1)

for i in month_enume:
    print(i[0], "month of the year it is:")
    print(i[1])
    print()


second = int(input("введите число секунд "))

days = second // 86400

second -= days * 86400

hours = second // 3600

second -= hours * 3600

minutes = second // 60

second -= minutes * 60

print("Days:", days, "Hours:", hours, "Minutes:", minutes, "Second:", second)
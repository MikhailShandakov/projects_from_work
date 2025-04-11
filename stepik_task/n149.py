ip = "10.0.1.1".split(".")

print(all([int(num.lstrip("0")) <= 255 for num in ip if num.isdigit()]))

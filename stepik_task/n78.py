second = int(input())

minutes, hours, days = 0, 0, 0

while second >= 60:
    minutes += 1
    if minutes == 60:
        hours += 1
        minutes = 0
        if hours == 24:
            days += 1
            hours = 0
    
    second -= 60
    
print("Days:", days, "Hours:", hours, "Minutes:", minutes, "Second:", second)
n = int(input())

result_list = []

FIRST_DIGIT = int(input())

for _ in range(n - 1):
    SECOND_DIGIT = int(input())
    result_list.append(FIRST_DIGIT + SECOND_DIGIT)
    FIRST_DIGIT = SECOND_DIGIT
    
print(result_list)
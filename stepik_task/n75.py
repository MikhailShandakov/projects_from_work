n = int(input())

summ, quan, mult, aver, first, end = 0, 0, 1, 0, 0, 0

Start_flag = n >= 10

while n > 0:
    summ += n%10
    quan += 1
    mult *= n%10
    
    if n // 10 == 0:
        first = n
        
    if Start_flag == True:
        end = n%10
        Start_flag = False
    
    n = n // 10
    
aver = summ/quan

ends = first + end

print(summ, quan, mult, aver, first, ends, sep="\n")
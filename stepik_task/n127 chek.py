def chek(word):
    
    flag = False
    
    while True:
        
        answer = input().lower()
        
        if answer.isalpha():
            if len(answer) == 1:
                if answer in [chr(i) for i in range(1072, 1072 + 32)]:
                    if answer in word:
                        flag = True
                    break
                  
            elif len(answer) > 1:
                if answer == word:
                    flag = True
                break
                
    if flag:
        return answer
    else:
        return "fail"

secret = "привет"

a = chek(secret)

print(a)
                
                

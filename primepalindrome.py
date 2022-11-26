print("Enter a digit below to get nth prime padindrome number")
n = int(input("Enter: "))
nth,num,i = 0,1,2 
while(nth<n):
    num+=1
    for i in range(2,num+1):
        a = str(num)
        if num%i==0:
            break
    if(i==num) and a == a[::-1]:
        nth += 1
print(num)

# Count the number which are divisible by 3 and 5. between 1 to 100
count =0
for i in range(1,101):
    if(i%3 == 0 and i%5 ==0):
        print("3 and 5 Divisible Values For 1-100 is :",i)
        count+=1
        
print("------------------")
print("Count Is :",count)
print("------------------")

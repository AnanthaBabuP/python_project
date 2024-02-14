tam = int(input("Enter Tamil Mark: "))		
eng = int(input("Enter English Mark: "))		
math = int(input("Enter Maths Mark: "))		
sci = int(input("Enter Sciance Mark: "))		
social = int(input("Enter Social Sciance Mark: "))
avg = (tam+eng+math+sci+social)/5
print("Average mark Is :",avg)
if(avg < 35):
    print("Additional class is required")
else:
    print("You are good to go")



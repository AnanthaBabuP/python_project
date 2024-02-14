salary = int(input("Enter Your Salary : "))
age = int(input("Enter Your Age :"))
if(salary >= 20000 or age <=25):
    loan_amount= int(input("Enter Loan Amount : "))
    if(loan_amount<=50000):
        print("You are Eligible for loan")
    else:
        print("Maximum Loan Amount is 50000")
else:
    print("You Are Not Eligible For Loan")


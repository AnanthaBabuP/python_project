score = int(input("Enter Score : "))
if (score < 30):
    print("Poor Student")
elif(score >= 30 and score < 70):
    print("Average Student")
elif(score >= 70 and score <= 100):
    print("Good Student")
else:
    print("Invalid Score")

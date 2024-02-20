print("Quiz") # Tittle
count=0    # Correct Quize Count
player = input('Do You Wand To play? ')     # Declare as pasible to play
if player.upper() != 'YES':  # Say No or anythig execution process will be stoped
     quit() 
print("Ok Let's Play")  # Type yes after run following Steps

question = input("How many days do we have in a week? ")    # Question No 1
if question == "7" or question == "seven":  # Check Answer and Answer is corect execut to if part
    print("Correct Answer") 
    count+=1
else :  # Else Run this else part
    print('Incorrect Answer:')
    print('Correct Answer is : seven')

question = input("In Which direction does the sun rise? ")    # Question No 2
if question.upper() == "EAST" :  # Check Answer and Answer is corect execut to if part
    print("Correct Answer")
    count+=1
else :  # Else Run this else part
    print('Incorrect Answer:')
    print('Correct Answer is : EAST')

question = input("What is our national bird? ")    # Question No 3
if question.upper() == "BEACOCK":  # Check Answer and Answer is corect execut to if part
    print("Correct Answer")
    count+=1
else :  # Else Run this else part
    print('Incorrect Answer:')
    print('Correct Answer is : BEACOCK')

question = input("Which is the fastest animal in the land? ")    # Question No 4
if question.upper() == "CHEETAH":  # Check Answer and Answer is corect execut to if part
    print("Correct Answer")
    count+=1
else :  # Else Run this else part
    print('Incorrect Answer:')
    print('Correct Answer is : CHEETAH')

question = input("Which animal is known as the 'Ship of the Desert'? ")    # Question No 5
if question.upper() == "CAMEL":  # Check Answer and Answer is corect execut to if part
    print("Correct Answer")
    count+=1
else :  # Else Run this else part
    print('Incorrect Answer:')
    print('Correct Answer is : CAMEL')

question = input("Which festival is called the festival of colours? ")    # Question No 6
if question.upper() == "HOLI":  # Check Answer and Answer is corect execut to if part
    print("Correct Answer")
    count+=1
else :  # Else Run this else part
    print('Incorrect Answer:')
    print('Correct Answer is : HOLI')


print('Quiz Over You Are ',count ,'correct for 6')  # Finally Executed corect answer for overall

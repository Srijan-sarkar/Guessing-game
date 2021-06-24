import random
value=random.randint(1,9)
print("Guess a Number between 1 to 9")
count = 0

while count < 5 :
    guess = int( input("Enter your guess") )

    if guess==value :
        print("congratulations you win")
        break; 

    elif guess>value :
        print("Your number is too big Enter a lower number than ", guess)

    else :
        print("Your number is too low Enter a higher number than ", guess)
    
    count= count+1

if not count <5:
    print("You lose the number was ", value)
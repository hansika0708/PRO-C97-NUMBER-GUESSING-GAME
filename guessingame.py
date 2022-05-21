import random
number = random.randint(1,9)
chancecount = 0
print("Guess a number between 1 and 9")
print("you have 5 chances")
while chancecount < 5 :
    guess = int(input("Enter your guess :"))
    chancecount = chancecount + 1
    if guess < number:
        print("you guess was too low , guess a number higher than " , guess)
    elif guess > number:
        print("your guess was too high, guess a number lower than" , guess)  
    elif guess == number:
        print("Congractulations you won!!!")
if not chancecount < 5:
    print("You lose! The number is ", number)


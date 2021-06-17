import random

print("HELLO! LET'S PALY A NUMBER GUESSING GAME")

num=random.randint(1,9)

chances=0

print("GUESS ANY NUMBER BETWEEN 1 TO 9")

while chances<5:
    guess=int(input("ENTER YOUR GUESS"))

    if guess == num:
        print("CORRECT")
        print("YOU WON!CONGRATULATIONS")
        print("👍😃")
        break

    elif guess < num:
        print("YOUR GUESS IS TOO LOW")
        print("GUESS A NUMBER HIGHER THAN THIS")

    else:    
        print("YOUR GUESS IS TOO HIGH")
        print("GUESS A NUMBER LOWER THAN THIS")

        chances+=1 

if chances==5 and guess!=num:
    print("YOU LOST")
    print("THE NUMBER WAS ",num)
    print("👎😪")        
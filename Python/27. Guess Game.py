a = 10
chance = 1
i=2
while chance <= 3:
    num = int(input("Enter a number : "))
    if num == a:
        print("You guessed the correct number..")
        break
    
    elif num != 10 and chance < 3:
        print(f"Try again.. {i} chances left..")

    else:
        print("Better luck next time..")
    
    i-=1
    chance += 1
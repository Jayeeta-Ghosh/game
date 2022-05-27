guess=int(input("Guess a number between 1-9"))
chances=0
number=7
while chances <5:
    if(not guess==number):
        if(guess>number):
            print("Guess number less than ",guess)      
        elif(guess<number):
            print("Guess the number more than ",guess)    
        else:
            print("Congratulations!!! You Won")
    break        
if(not chances<5):
    print("You lose!!! The number is",number)    
                        


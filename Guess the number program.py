import random

count = 0
attempt = 3


def hilo():
    if (guess < num):
        print ('the number you have guessed is too low','\n')
    if (guess > num):
        print ('the number youve guessed is too high')
        
        
print ('WELCOME','\n')

while True:
    try:
        num = random.randint(0,20)
        guess = int(input('Insert your choice, it`s between 0-20:'))
        if num == guess:
            print('You won')
#while loop inserted in order to repeat the attempt of the user            
        while num != guess:
#attempt counter            
            count += 1
            print ("you have:", attempt - count,"attempt more","\n")
            if count == (3):
                print ("bye bye , too many attempt")
                
                break
            
            hilo()
            guess = int(input("try again  - ", ))
            if guess == num:
                print("correct answer")
                
#break inserted to exit the while loop        
        break

    except:
        print("numbers nothing else")
    

input("Press Enter to leave")
# Favour Achara guessing game
name=input('What\'s your name dear user: ')
secret_name='achara'
print('Welcome',name,'to Achara\'s Guessing Game')
tries=1

for i in range(3): # iterates the guess variable, the if,elif,nested if and else statements three times if  the
    # conditions are satisfied.
    guess=input("Guess my name: ")
    if guess==secret_name:
        print('Congratulations ',name,' you got my name correctly. YOU WIN!!!!')
        game_over=True
    elif tries == 2:
        print(name, 'you are on your last try so think hard and well. Goodluck')
        print('Hint: my surname')
    elif tries==3:
        print('Sorry',name,'but unfortunately you have reached the total tries limit given to you',tries,'/3,. So YOU LOST!!!!!')
    else:
        print('Try again',name)
    tries += 1

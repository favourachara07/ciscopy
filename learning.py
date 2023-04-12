def acharatrivia():
    totalpts=0
    #Level 1
    print('Welcome to Achara Trivia game'
          'This trivia game is based on One piece'
          'There are ten levels in this trivia game'
          'All levels will will cover the every memeber of straw-hats'
          'You receive 5pts for every level you pass'
          'I wish you the best if you are a big fan of one piece like i am'
          'GOOD LUCK!!!')
    ques1=input('Who gave luffy his strawhat\n'
                'a. Shanks\n'
                'b. Gol D. Roger\n'
                'c. Fire Fist Ace\n'
                'd. Whitebeard\n'
                'Ans: ')
    if ques1== 'Shanks':
        print('YOU ARE CORRECT. THAT WAS QUITE A SIMPLE ONE\n'
              'Each level promises to be much harder '
              'You got 5pts')
        totalpts+=5
    else:
        print('YOU FAILED. BRO LIKE I CANT IMAGINE YOU FAILING THIS\n'
              'If you were a true one piece fan this wouldn\'t have been trouble\n'
              'Oh well you lost the game, come back tomorrow to restart it')
        acharatrivia()
    ques2 = input('Which arc did Luffy and Usopp fight\n'
                  'a. Enies Lobby arc\n'
                  'b. Marineford arc\n'
                  'c. Water 7 arc\n'
                  'd. Skypiea arc\n'
                  'Ans: ')
    if ques2 == 'Water 7 arc':
        print('YOU ARE CORRECT. THAT WAS QUITE A SIMPLE ONE\n'
              'Each level promises to be much harder '
              'You got 5pts')
        totalpts += 5
    else:
        print('YOU FAILED. BRO LIKE I CANT IMAGINE YOU FAILING THIS\n'
              'If you were a true one piece fan this wouldnt have been trouble\n'
              'Oh well you lost the game, come back tomorrow to restart it')


acharatrivia()
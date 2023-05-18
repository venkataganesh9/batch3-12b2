import random
'''
   rock:1
   paper:2
   scissors:3
   1 x 2:2  paper wins
   2 x 3:3  scissors wins
   1 x 3:1  rock wins
'''
class rockpaper:
    def __init__(self):
        self.player_score=0
        self.computer_score=0
        self.player_name=str(input('Hello I am Jarvis, Please Enter Your Name: '))
    def win_or_loose(self,player_option,computer_option):
        print()
        if (player_option in ['1',1,'rock','Rock','r','R','ROCK'] and computer_option==3) or (player_option in ['2',2,'paper','Paper','PAPER','P','p'] and computer_option==1) or (player_option in ['3',3,'scissors','Scissors','SCISSORS','s','S'] and computer_option==2):
            self.player_score+=1
            if (player_option in ['1',1,'rock','Rock','r','R','ROCK'] and computer_option==3):
                print(self.player_name+' choice is Rock and Jarvis choice is Scissors')
                print('Rock beats Scissors')
            elif (player_option in ['2',2,'paper','Paper','PAPER','P','p'] and computer_option==1):
                print(self.player_name+' choice is Paper and Jarvis choice is Rock')
                print('Paper beats Rock')
            else:
                print(self.player_name+' choice is Scissors and Jarvis choice is Paper')
                print('Scissors beats Paper')
            print(self.player_name+' wins in this round')
        elif (player_option in ['1',1,'rock','Rock','r','R','ROCK'] and computer_option==1) or  (player_option in ['2',2,'paper','Paper','PAPER','P','p'] and computer_option==2) or (player_option in ['3',3,'scissors','Scissors','SCISSORS','s','S'] and computer_option==3):
            print()
            if computer_option==2:
                print(self.player_name+' choice is Paper and Jarvis choice is Paper')
            elif computer_option==1:
                print(self.player_name+' choice is Rock and Jarvis choice is Rock')
            else:
                print(self.player_name+' choice is Scissors and Jarvis choice is Scissors')
            print('It is a Draw between Jarvis and '+self.player_name+' in this round')
        elif player_option not in ['1',1,'rock','Rock','r','R','ROCK','2',2,'paper','Paper','PAPER','P','p','3',3,'scissors','Scissors','SCISSORS','s','S']:
            raise exception        
        else:
            print()
            if computer_option==2:
                print(self.player_name+' choice is Rock and Jarvis choice is Paper')
                print('Paper beats Rock')
            elif computer_option==1:
                print(self.player_name+' choice is Scissors and Jarvis choice is Rock')
                print('Rock beats Scissors')
            else:
                print(self.player_name+' choice is Paper and Jarvis choice is Scissors')
                print('Scissors beats Paper')
            self.computer_score+=1
            print('Jarvis Wins in This Round')

yes=1
try:
  while yes:
    print()
    obj=rockpaper()
    print()
    print("Enter '1' or 'rock' or 'Rock' or 'ROCK' or 'r' or 'R' for choosing Rock\nEnter '2' or 'PAPER' or 'Paper' or 'paper' or 'p' or 'P' for choosing Paper\nEnter '3' or 'scissors' or 'Scissors' or 'SCISSORS' or 'S' or 's' for choosing Scissors")
    print()
    n=int(input('Enter no of rounds you want to play: '))
    print()
    for i in range(n):
        print('Let us begin the round')
        computer_option=random.randint(1,3)
        obj.win_or_loose(str(input('Enter your option: ')),computer_option)
    print()
    print('Game Over')
    if obj.player_score>obj.computer_score:
        print(str(obj.player_name)+' Won This Game With '+str(obj.player_score)+'/'+str(n)+'\n'+'Jarvis Lost This Game With '+str(obj.computer_score)+'/'+str(n))
    elif obj.player_score==obj.computer_score:
        print('It is Draw between '+obj.player_name+' and Jarvis')
    else:
        print('Jarvis Won This Game With '+str(obj.computer_score)+'/'+str(n)+'\n'+str(obj.player_name)+' Lost This Game With '+str(obj.player_score)+'/'+str(n))
    yes=int(input('enter 0 if you want to quit: '))
except:
    print('Enter Input in Given Format')

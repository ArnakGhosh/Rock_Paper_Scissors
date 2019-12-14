import getpass, random
from datetime import datetime
from os import system, name
#asd=getpass.getpass(prompt='enter text : ', stream=None)
#print(asd)
#for i in range(10): print(random.randint(1,3))
playScore=dict()
def clear():
    if name=='nt': system('cls')
    else : system('clear')
def getTitle():
    print('''
********************************************************
****                                                ****
****  THE NEW ROCK, PAPER, SCISSORS GAME IN PYTHON  ****
****                                                ****
****              Version : 0.0.1                   ****
********************************************************
''')
def getMainMenu():
    print('''
.___________________.
|1. Start New Game  |
|2. Instructions    |
|3. Credits         |
|4. Exit            |
|___________________|
''')
def getPlayMenu():
    print('''
._____________________.
|1. Continue          |
|2. Back to Main Menu |
|_____________________|
''')
def playerDets():
    clear()
    getTitle()
    pl=input('Please enter your name : ')
    print(pl,', welcome to the game!')
    asd=input('Press enter to continue')
    return pl
def mainMenu():
    clear()
    getTitle()
    getMainMenu()
    choice=input('Please Enter your Choice : ')
    if choice not in ('1','2','3','4'):
        return True
    else:
        return choice
def play(a,b,c,d):
    ll=''
    playDic={'R':1,'S':0,'P':-1}
    clear()
    getTitle()
    diff=playDic.get(a)-playDic.get(b)
    if diff==1 or diff==-2:
        print(c,'chose',a,'and',d,'chose',b,', so',c,' WINS!')
        ll=c
    elif diff==-1 or diff==2:
        print(d,'chose',b,'and',c,'chose',a,', so',d,' WINS!')
        ll=d
    else:
        print(c,'and',d,'chose',a,'and',b,', so it is a TIE!')
        ll='TIE'
    input('Press a key to continue')
    return ll
def getScore(u1,u2):
    c1=0
    c2=0
    clear()
    getTitle()
    for i,v in enumerate(playScore):
        print('Turn',v,': Winner was',playScore.get(v))
        if playScore.get(v)==u1: c1+=1
        elif playScore.get(v)=='TIE' or playScore.get(v)=='':
            c2=c2
            c1=c1
        else: c2+=1
    print('\n\n')
    if c1>c2:
        print(u1,'has won the game with',c1*10,'points, CONGRATULATIONS!')
    elif c2>c1:
        print(u2,'has won the game with',c2*10,'points, CONGRATULATIONS!')
    else:
        print('Its A Tie!')
    input('Press Enter to continue')
    playScore.clear()
def singlePlayer():
    winner=''
    life3=True
    count=1
    player1=playerDets()
    hostUser=getpass.getuser()
    while life3==True and count<=5:
        clear()
        getTitle()
        print('TURN ',count,' ##')
        print('To quit the game, enter q')
        print('R for Rock, P for paper, S for scissors, choose wisely!')
        plChoice=getpass.getpass(prompt='Enter your Choice : ', stream=None)
        if plChoice=='q':
            life3=close()
        elif plChoice in ('R','P','S'):
            hostChoice=random.choice('RSP')
            winner=play(plChoice,hostChoice,player1,hostUser)
            life3=True
        elif count=='5':
            life3=False
        else:
            clear()
            getTitle()
            print('Wrong choice, you have ',(5-count),' turns!')
            input('Press a key to continue ')
        playScore[count]=winner
        winner=''
        count+=1
    getScore(player1,hostUser)
    return True
def multiPlayer():
    pass
def newGame():
    clear()
    gamedic={1:singlePlayer, 2:multiPlayer}
    life2=True
    while life2==True:
        clear()
        getTitle()
        getPlayMenu()
        game=input('Please Enter your Choice : ')
        if game in ('1'):
            life2=gamedic.get(int(game))()
        elif game=='2':
            life2=False
        else:
            life2=True
    if life2==False: return True  
def instructions():
    clear()
    getTitle()
    print('''
Very simple to play, you can press either of these 3
options : R/P/S for Rock/Paper/Scissor. Please note
that the letters need to be entered in ALL CAPS, oth-
erwise the program will not take the input as valid
and you will loose your chance.

The Program decides on the criteria that:

ROCK beats SCISSORS
SCISSORS beats PAPER
PAPER beats ROCK

For every turn that you win, you get rewarded with 10
points. At the end of 5 turns, the player with maximum
score wins. By players, I define only you and your
big, black and lonely python shell! (as of now, ;) )

I guess that is the correct rule, please get it 
verified by any kid and change the logic by yourself
HaHaHa!
        ''')
    input('Press Enter if you wish to return to main menu')
    return True
def credit():
    clear()
    getTitle()
    print('''
This code has been developed by myself, but that would
not have been possible without encouragement and supp-
ort from my friends and colleagues, a big shout out to
them. 

However, the real credit goes to Guido Van Rossum
for authoring an immensely powerful, yet simple lang-
guage as Python and all the other unsung heroes whose
numerous blogs and videos had helped me a lot to unde-
rstand the language use it wisely.

This game was developed solely as an experiment, so
neither do I take any responsibility nor any 
ownership for malfunctioning / bugs in the code and 
should be used for fun and fun only.

 This is free for all
        ''')
    input('Press Enter if you wish to return to main menu')
    return True
def close():
    clear()
    getTitle()
    res=input('Do you wish to quit? (Y/N) : ')
    if res=='Y':
        return False
    else:
        return True
def main():
    clear()
    life=True
    choice=None
    choiceDic={1:newGame, 2:instructions, 3:credit, 4:close}
    while life==True:
        choice=mainMenu()
        if choice==True:
            life=choice
        else:
            choice=int(choice)
            life=choiceDic.get(choice)()
if __name__ == '__main__':
    main()

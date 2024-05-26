#modules used throughout
import emoji #to print emojis
import random #generate a word randomly from lists
from colorama import Fore, Back, init, Style #to format the color of text
init()

#function that prints tha art of hangman
def hangman_art(art):
    if art==1:
        print(" ____"," |  |","\O/ |","    |","    |",sep="\n")
    elif art==2:
        print(" ____"," |  |","\O/ |"," |  |","    |",sep="\n")
    else:
        print(" ____"," |  |","\O/ |"," |  |","/ \ |",sep="\n")

#Hangman part of the TIC TAC MAN
def hangman (result):
    #lists that will be used for the words to be gussed
    cities = ['Karachi', 'Islamabad', 'London', 'Tokyo', 'Delhi', 'Shanghai', 'Berlin', 'Zurich', 'Mumbai', 'Chennai']
    animals = ['Tiger', 'Zebra', 'Peacock', 'Ostrich', 'Iguana', 'Nightingale']
    food = ['Pretzel', 'Pancakes', 'Baguette', 'Croissant', 'Pizza', 'Burger', 'Omelette']
    default = ('_' + ' ')
    score = 0
    print()
    print(emoji.emojize(":skull_and_crossbones:"), Fore.BLUE+" Welcome to the second part of TIC TAC MAN", emoji.emojize(":skull_and_crossbones:"))
    print(Style.RESET_ALL)

    #conditions to ensure that the winner gets 3 words
    if result == "Yes" or result == 'yes':
        num = 3
    elif result == "No" or result == 'no':
        num = 2
    else:
        num = 0
    for j in range(num):
        art=0
        if j == 0:
            lst = cities
            category = "city"
        elif j == 1:
            lst = animals
            category = "animal"
        elif j == 2:
            lst = food
            category = "food"
        i = random.choice(lst)
        lives = 3
        n = ''
        used = ''
        print()
        print('Word number:', j + 1, "(" + category + ")")
        print (default * len(i))
        #takes guess letters as input
        while lives > 0 and len(n) < len(i):
            print ()
            guess = input("Please enter you guess for the word!")
            print()
            while guess.isalpha() == False or len(guess) > 1 or guess.lower() in used or guess.upper() in used:
                print()
                print(emoji.emojize(":face_with_raised_eyebrow:")*3, 'Character should be a single alphabet only and not used before. Re-enter:', emoji.emojize(":face_with_raised_eyebrow:")*3)
                guess = input()
            if guess.lower() not in i and guess.upper() not in i:
                lives -= 1
                print()
                print(emoji.emojize(":disappointed_face:"),Fore.RED+'Wrong!',emoji.emojize(":disappointed_face:"))
                print(Style.RESET_ALL)
                art+=1
                hangman_art(art)
            else:
                for j in range(len(i)):
                    if i[j] == guess.lower() or i[j] == guess.upper():
                        n += i[j]
                        print(i[j], end=' ')
                    elif i[j] in n:
                        print (i[j], end=' ')
                    else:
                        print(default, end='')
            used += guess
        if len(n) == len(i):
            print()
            print(emoji.emojize(":party_popper:")*3,'Congratulations! You have guessed the word correctly',emoji.emojize(":party_popper:")*3)
            print()
            score += 1
        elif lives == 0:
            print()
            print(emoji.emojize(":disappointed_face:")*3,Fore.RED+'No more lives left', emoji.emojize(":disappointed_face:")*3)
            print(Style.RESET_ALL)
            hangman_art(art)
        lst.remove(i)
    return score

#The main game that has TIC TAC TOE as a starting competetition
print(emoji.emojize(":multiply:"),emoji.emojize(":hollow_red_circle:"),Fore.BLUE+"Welcome to the first part of TIC TAC MAN",emoji.emojize(":hollow_red_circle:"),emoji.emojize(":multiply:"))
print(Style.RESET_ALL)

#initializing values
arr= [[" " for col in range (3)]for row in range(3)]

#it allows use to enter positions as single digit integer rather than rows and columns
dic={1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2]}
a= " "
turn= 0
b=0
d=1
temp=" "
turns= 0
while True:
    #take input from player 1
    if d == 1:
        print()
        y= int(input("Enter the place you want to put your mark, player 1 "))
        print()
        while y<0 or y>9 or arr[dic[y][0]][dic[y][1]] == "O":
            y = int(input("Error!!!enter the place you want to put your mark, player 1 "))
        arr[dic[y][0]][dic[y][1]]= "X"
        c= 1
        #to ensure that the player one gets to take 5 turns
        turn = turn + 1
        #ensure that the game works for 9 turns
        turns=turns+1
    #for player 2
    if b == 1:
        if turn != 5:
            print()
            y= int(input("Enter the place you want to put your mark, player 2 "))
            print()
            while y<0 or y>9 or arr[dic[y][0]][dic[y][1]] == "X":
                y = int(input("Error!!!enter the place you want to put your mark, player 2 "))
            arr[dic[y][0]][dic[y][1]]= "O"
            c= 1
            turns = turns + 1
    #comparisons to check if win criteria is met
    if c == 1:
        for row in range(3):
            col = 0
            if arr[row][col] == arr[row][col + 1] and arr[row][col + 1] == arr[row][col + 2]:
                if arr[row][col] == "X":
                    a= "PLAYER 1 WINS"
                elif arr[row][col] == "O":
                    a= "PLAYER 2 WINS"
        for col in range(3):
            row = 0
            if arr[row][col] == arr[row + 1][col] and arr[row + 1][col] == arr[row + 2][col]:
                if arr[row][col] == "X":
                    a= "PLAYER 1 WINS"
                elif arr[row][col] == "O":
                    a= "PLAYER 2 WINS"
        row = 0
        col = 0
        if arr[row][col] == arr[row + 1][col + 1] and arr[row + 1][col + 1] == arr[row + 2][col + 2]:
            if arr[row][col] == "X":
                a= "PLAYER 1 WINS"
            elif arr[row][col] == "O":
                a= "PLAYER 2 WINS"
        row = 0
        col = 2
        if arr[row][col] == arr[row + 1][col - 1] and arr[row + 1][col - 1] == arr[row + 2][col - 2]:
            if arr[row][col] == "X":
                a= "PLAYER 1 WINS"
            elif arr[row][col] == "O":
                a= "PLAYER 2 WINS"
        for row in range(3):
            for col in range(3):
                print(arr[row][col], end="|")
            print()
    #switches values so that after every turn the check for winning is carried out
        temp = d
        d = b
        b = temp
    #prints the winning result
    if a=="PLAYER 1 WINS" or a=="PLAYER 2 WINS":
        print()
        print(emoji.emojize(":party_popper:")*3,Fore.RED+a,emoji.emojize(":party_popper:")*3)
        print()
        break
    #prints if game is a draw or not
    if turns==9:
        print()
        print(emoji.emojize(":zipper-mouth_face:")*3,(Fore.RED+" GAME IS A DRAW"),emoji.emojize(":zipper-mouth_face:")*3)
        print()
        break

#This part allows both players to play hangman
print(Style.RESET_ALL)
result = input(Fore.YELLOW+"Player 1, Did you win the last game? (Yes/No)")
score1=(hangman(result),1)
result = input(Fore.YELLOW+"Player 2, Did you win the last game? (Yes/No)")
score2=(hangman(result),2)

#figueres out the winner
if score1[0]>score2[0]:
    print()
    print(emoji.emojize(":hourglass_not_done:")*3,"Time for results",emoji.emojize(":hourglass_not_done:")*3)
    print()
    print(emoji.emojize(":party_popper:")*3,Fore.YELLOW+"The Victor is player:",score1[1],emoji.emojize(":party_popper:")*3)
elif score1[0]<score2[0]:
    print()
    print(emoji.emojize(":hourglass_not_done:")*3,"Time for results",emoji.emojize(":hourglass_not_done:")*3)
    print()
    print(emoji.emojize(":party_popper:")*3,Fore.YELLOW+"The Victor is player:",score2[1],emoji.emojize(":party_popper:")*3)
else:
    print()
    print(emoji.emojize(":hourglass_not_done:")*3,"Time for results",emoji.emojize(":hourglass_not_done:")*3)
    print()
    print(Fore.YELLOW+"Game is a Draw")

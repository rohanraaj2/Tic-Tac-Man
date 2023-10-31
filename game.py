arr= [[" " for col in range (3)]for row in range(3)]

#it allows use to enter positions as single digit integer rather than rows and columns
dic={1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2]}
winner = ''
turn = 0
b = 0
d = 1
temp = " "
turns= 0
while True:
    #take input from player 1
    if d == 1:
        print()
        y= int(input("Enter the place you want to put your mark, player 1 "))
        print()
        while y<0 or y>9 or arr[dic[y][0]][dic[y][1]] == "O":
            y = int(input("Error!!!enter the place you want to put your mark,5 player 1 "))
        arr[dic[y][0]][dic[y][1]]= "X"
        c= 1
        #to ensure that the player one gets to take 5 turns
        turn = turn + 1
        #ensure that the game works for 9 turns
        turns = turns + 1
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
                    winner = "PLAYER 1 WINS"
                elif arr[row][col] == "O":
                    winner = "PLAYER 2 WINS"
        for col in range(3):
            row = 0
            if arr[row][col] == arr[row + 1][col] and arr[row + 1][col] == arr[row + 2][col]:
                if arr[row][col] == "X":
                    winner = "PLAYER 1 WINS"
                elif arr[row][col] == "O":
                    winner = "PLAYER 2 WINS"
        row = 0
        col = 0
        if arr[row][col] == arr[row + 1][col + 1] and arr[row + 1][col + 1] == arr[row + 2][col + 2]:
            if arr[row][col] == "X":
                winner = "PLAYER 1 WINS"
            elif arr[row][col] == "O":
                winner = "PLAYER 2 WINS"
        row = 0
        col = 2
        if arr[row][col] == arr[row + 1][col - 1] and arr[row + 1][col - 1] == arr[row + 2][col - 2]:
            if arr[row][col] == "X":
                winner = "PLAYER 1 WINS"
            elif arr[row][col] == "O":
                winner = "PLAYER 2 WINS"
        for row in range(3):
            for col in range(3):
                print(arr[row][col], end="|")
            print()
    #switches values so that after every turn the check for winning is carried out
        temp = d
        d = b
        b = temp
    #prints the winning result
    if winner =="PLAYER 1 WINS" or winner =="PLAYER 2 WINS":
        print (winner)
        break
    #prints if game is a draw or not
    if turns==9:
        print("Draw!")
        break

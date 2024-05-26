import random
words = ['attend', 'pursue', 'unfold', 'beamed', 'campus']
cities = ['Karachi', 'Islamabad', 'London', 'Tokyo', 'Delhi', 'Shanghai', 'Berlin', 'Zurich']

default = ('_' + ' ')
used_words = []

for j in range(7):
    i = random.choice(words)
    while i in used_words:
        i = random.choice(words)
    used_words.append(i)
    l = 3
    n = ''
    used = ''
    print ('Word number:', j + 1)
    print (default * len(i))
    while l > 0 and len(n) < len(i):
        print ()
        guess = input()
        guess = guess.lower()
        while guess.isalpha() == False or len(guess) > 1 or guess in used:
            print ('Character should be a single alphabet only and not used before. Re-enter:')
            print ()
            guess = input()
            guess = guess.lower()
        if guess not in i:
            l -= 1
            print ('Wrong!')
        else:
            for j in range(len(i)):
                if i[j] == guess:
                    n += guess
                    print (i[j], end = ' ')
                elif i[j] in n:
                    print (i[j], end = ' ')
                else:
                    print (default, end = '')
        used += guess
    if len(n) == len(i):
        print ()
        print ('Congratulations! You have guessed the word correctly')
    elif l == 0:
        print ('No more lives left')

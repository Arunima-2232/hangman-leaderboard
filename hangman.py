import random, sys
import mysql.connector
def inform():
    global name
    global ID
    global score
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="11intelli22tiate", database="leaderboard")
    cursor=mydb.cursor()
    sql="insert into scores(Player_ID, name, Hints_left, Chances_left, Score) values(%s,%s,%s,%s,%s)"    
    val=(ID, name, HINT, chances, score)
    cursor.execute(sql,val)
    mydb.commit()
    cursor.execute("select * from scores")
    for x in cursor:
        print(x)
    mydb.commit()
def again():
    global inco
    global name
    global word_st
    str(word)
    global score
    score=chances+guessed+HINT
    if inco==5:
        print("\nGAME LOST. The word was", word_st)
        print("Your score is", score)
        c=int(input("Enter 1 to see leaderboard: "))
        if c==1:
            inform()
        print("Thank you for playing",name,"! We expect you back again!")
        sys.exit()
    else:
        if timeplayed<3:
            print("\nYOU GUESSED THE WORD!")
            next=input("Enter Y to guess a new word, N to quit the game: ")
            if next.upper()=="Y":
                chosen()
            elif next.upper()=="N":
                print("Your score is", score)
                c=int(input("Enter 1 to see leaderboard: "))
                if c==1:
                    inform()
                print("Thank you for playing",name,"! We expect you back again!")
                sys.exit()
            else:
                print("YOU'VE GUESSED ALL WORDS!")
                print("Your score is", score)
            c=int(input("Enter 1 to see leaderboard: "))
            if c==1:
                inform()
            print("Thank you for playing",name,"! We expect you back again!")
            sys.exit()  
def hangman():
    global inco
    if inco==1:
        print("   ___ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     | \n"
              "  |      \n"
              "  |      \n"
              "_|_\n")
    elif inco==2:
        print("   ___ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     O \n"
              "  |     | \n"
              "  |      \n"
              "  |      \n"
              "_|_\n")
    elif inco==3:
        print("   ___ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |      \n"
              "_|_\n")  
    elif inco==4:
        print("   ___ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |     | \n"
              "_|_\n")
    elif inco==5:
        print("   ___ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |    / \ \n"
              "_|_\n")
    print("You have ",5-inco," chance(s) left")
    player()
def Hint():
    hint=''
    if word_st=='burden':
        hint='something that is heavy to carry'
    elif word_st=='change':
        hint='alter or modify'
    elif word_st=='acting':
        hint='the job of performing in films or plays'
    elif word_st=='closed':
        hint='not open'
    elif word_st=='client':
        hint='a desktop computer or workstation that can obtain information and applications from a server.'
    elif word_st=='barely':
        hint='only just; almost not'
    elif word_st=='bought':
        hint='past tense of buy'
    return hint
def player():
    global inco
    global clue
    global guessed
    global chances
    global HINT
    global li
    l=0
    while inco<5 and word_displayed!=word:
        print("\nThis is the Hangman Word: ",word_displayed)
        inp=input("Enter a letter you think is in the word.\n")
        l=len(inp)
        inp=inp.lower()
        if inp in li:
            inp=input("This letter has already been entered. Try again. \n")
        if inp!="hint":
            li.append(inp)
        if inp in word:
            print("Correct!")
            guessed+=1
            indexs=word.index(inp)
            count=word.count(inp)
            g=0
            if count>1:
                while count>1:
                    word_displayed[indexs]=inp
                    g=indexs
                    indexs=word.index(inp,indexs+1)
                    count=count-1
                    word_displayed[indexs]=inp
            word_displayed[indexs]=inp
        elif inp not in word and inp!="hint":
            inco=inco+1
            chances-=1
            if inco<5:
                print("Wrong guess. Try again!")
            hangman()
        elif inp=="hint":
            if HINT==1:
                print("\nHINT: ",Hint())
                HINT-=1
                inco+=1
            else:
                print("You've already asked for the hint")
    else:
        again()        
def chosen():
    global timeplayed
    timeplayed+=1
    global ind
    ind+=1
    global li
    li=[]
    global word
    global word_st
    global word_displayed
    word=word_list[ind]
    word_displayed=list()
    for i in range(0,len(word)):
        word_displayed.append("_")
    word_st=word
    word=list(word)
    player()
def ready():
    global inco
    inco=0
    global name
    print("\nINSTRUCTIONS: \n\nA word will be chosen for you at random.")
    print("You will be given a number of dashes equivalent to the number of letters in the word.")
    print("You may ask for a clue by typing hint but doing so will add one element to the hangman's gallows.")
    print("If your guessed letter is a part of the word it will be shown in its correct positions.")
    print("The game ends when the word has been guessed or the hangman figure is complete (you've made 5 incorrect guesses).\n")
    print("The game is about to start\nLet's play Hangman!\n")
    chosen()    
global word_list
global name
global ind
global HINT
global chances
global guessed
global timeplayed
global ID
score=0
guessed=0
HINT=1
chances=5
ind=-1
timeplayed=0
word_list=['burden','change','editor','closed','client','barely','bought']
random.shuffle(word_list)
name=input("Please enter your name.\n")
ID=int(input("Please enter a 3 digit player ID. \n"))
print("Welcome",name,"!")
ready()

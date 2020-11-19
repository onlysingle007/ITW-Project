################################################
#rock paper scissors
import random
 
#define basic variables and list for computer to choose from
o_list=["r","p","s"]
c_s=0
p_s=0
ch="R"
c_ch="f"
name="rps"
 
 
def get_ch():
    """This functon is called for taking user input"""
    global ch #define ch as a global variable
    x=0
    while x==0:
        print("Press \"r\" for rock, \"p\" for paper and \"s\" for scissors")
        ch=input("Enter your choice: ")
        if ch=="r" or ch=="p" or ch=="s" or ch=="R" or ch=="P" or ch=="S":
            x=x+1
        else:
            print("Enter valid input")
    return ch #return the user choise
 
 
def com_ch(o_list):
    """This function generates a random choise for computer from the list defind previously"""
    global c_ch
    c_ch=random.choice(o_list)
    return c_ch
 
 
def rps():
    """This is the main Rock Paper Scissor function"""
    global c_s
    global p_s
    ch=get_ch() #obtained user input by calling the "get_ch()" function
    c_ch=com_ch(o_list) #obtained the computer choise by calling the "com_ch()" function
    
    #converted the choises to upper case for simplicity
    p_c=ch.upper()
    c_c=c_ch.upper()
    
    #print the selected choise
    if c_c=="R":
        print("\nComputer choise: ROCK")
    if c_c=="P":
        print("\nComputer choise: PAPER")
    if c_c=="S":
        print("\nComputer choise: SCISSORS")
    if p_c=="R":
        print("You choise: ROCK")
    if p_c=="P":
        print("You choise: PAPER")
    if p_c=="S":
        print("You choise: SCISSORS")
    
    #same choice
    if p_c==c_c:
        print("Both you and computer choose same so no one gets a point")
    
    #user choose ROCK
    if p_c=="R":
        if c_c=="P":
            print("Computer won")
            c_s=c_s+1
        elif c_c=="S":
            print("You won")
            p_s=p_s+1
    
    #user choose PAPER
    if p_c=="P":
        if c_c=="S":
            print("Computer won")
            c_s=c_s+1
        elif c_c=="R":
            print("You won")
            p_s=p_s+1
    
    #user choose SCISSORS
    if p_c=="S":
        if c_c=="R":
            print("Computer won")
            c_s=c_s+1
        elif c_s=="P":
            print("You won")
            p_s=p_s+1
    
    #Displaying final score after the round
    print("\nComputer score:",c_s,"\nYour score:",p_s)
    
    #asking to play again
    ag=input("\nPress \"Y\" to play again or Enter anything else to exit :")
    again=ag.upper()
    if again == "Y":
        print("\n")
        rps()
 
        
########################################################
#HANGMAN
 
#The below list contains the word that are to be guessed by the user
word_list = ["math", "numpy", "pandas", "tkinter", "matplotlib", "pyaudio"]
 
def get_word(word_list):
    """The function to genetarte random word form the above list"""
    word = random.choice(word_list)
    return word.lower()
 
def play(word):
 
    """This is the main hangman game function"""
    word_completion = "_ " * len(word)
    guessed = False         #Initialising guessed with False as nothing has been guessed
    guessed_letters = []    #All the guessed alhabets are stored here
    guessed_words = []      #All the guessed words are stored here
    tries = 6
 
    print("""\nIn this game you need to guess the name of a python module which will
exactly fit in the blank spaces provided. You have limited tries. 
You can guess till a hangman is formed, i.e., 6 tries.\n""")
    print(display_hangman(tries))   #Calls the functon to display the hangman graphic status according to the tries left
    print(word_completion)
    print("\n")
 
    #Taking input from the user and verifying if his guess is correct or not.
    while not guessed and tries > 0:
        guess = input("Guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():
 
            if guess in guessed_letters:
                print("you already tried", guess, "!")
 
            elif guess not in word:
                print(guess, "isn't in the word :(")
                tries -= 1
                guessed_letters.append(guess)
 
            else:
                print("Nice one,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
 
                for index in indices:
                    word_as_list[index*2] = guess
                word_completion = "".join(word_as_list)
 
                if "_" not in word_completion:
                    guessed = True
 
        elif len(guess) == len(word) and guess.isalpha():
 
            if guess in guessed_words:
                print("You already tried ", guess, "!")
 
            elif guess != word:
                print(guess, " is not the Word :(")
                tries -= 1
                guessed_words.append(guess)
 
            else:
                guessed = True
                word_completion = word
 
        else:
            print("invalid input")
 
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
 
    #Printing the end result
    if guessed:
        print("Good Job, you guessed the word!")
    else:
        print("I'm sorry, but you ran out of tries. The word was " + word + ". Maybe next time!")
 
 
 
 
def display_hangman(tries):
    """This is used to get the image of hangman according to the number of tries left"""
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[tries]
 
def hangman():
    """This used to call the required function to play the game"""
    word = get_word(word_list)
    play(word)
    
    #asking to play again
    while input("Press \"Y\" to play again or Enter anything else to exit :").upper() == "y":
        word = get_word(word_list)
        play(word)
 
#################################################
# welcome to the main menu
while True:
    print("\nMain Menu\n")
    t=(input("Enter (1) to play \"ROCK PAPER SCISSORS\" game\nEnter (2) to play \"HANGMAN\" game\nor Enter anything else to exit\n"))
    
    if t=="1":
        print("\nPlaying \"ROCK PAPER SCISSORS\"...")
        rps()
        
    elif t=="2":
        print("\nPlaying \"HANGMAN\"...")
        hangman()
        
    else:
        print("Exiting")
        break

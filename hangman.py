import string
from words import choose_word
from images import IMAGES

# End of helper code
# -----------------------------------

def get_hint(secret_word):
    import random
    letter_secret=[]
    for x in secret_word:
        letter_secret.append(x)
        hint=random.choice(letter_secret)
    print hint

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: return True kare agar saare letters jo ki user ne guess kiye hai wo secret_word mai hai, warna no
      False otherwise
    '''
    if secret_word==get_guessed_word(secret_word, letters_guessed):
        return True
    return False

# Iss function ko test karne ke liye aap get_guessed_word("kindness", [k, n, d]) call kar sakte hai
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess kar raha hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek string return karni hai jisme wo letters ho jo sahi guess huye ho and baki jagah underscore ho.
    eg agar secret_word = "kindness", letters_guessed = [k,n, s]
    to hum return karenge "k_n_n_ss"
    '''

    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
    eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
    jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
    '''
    import string
    letters_left = string.ascii_lowercase
    available_letters=""
    for letter in letters_left:
        if letter not in letters_guessed:
            available_letters+=letter
    return available_letters

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Hangman game yeh start karta hai:

    * Game ki shuruaat mei hi, user ko bata dete hai ki
      secret_word mei kitne letters hai

    * Har round mei user se ek letter guess karne ko bolte hai

    * Har guess ke baad user ko feedback do ki woh guess uss
      word mei hai ya nahi

    * Har round ke baar, user ko uska guess kiya hua partial word
      display karo, aur underscore use kar kar woh letters bhi dikhao
      jo user ne abhi tak guess nahi kiye hai

    '''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secret_word)) + " letters long."
    print ""

    user_difficulity=raw_input("Aap kitna deficult khelna cahate ho\n1) Easy \n2)Normal \n3)Hard \nplease choice 1 , 2 and 3\n")

    if user_difficulity=="1":
        remaining_lives=8
        index_of_IMAGES=[0,1,2,3,4,5,6,7]
    else:
        if user_difficulity=="2":
            remaining_lives=6
            index_of_IMAGES=[0,1,2,3,5,7]
        else:
            remaining_lives=4
            index_of_IMAGES=[1,3,5,7]

    letters_guessed = []
    i=0
    while remaining_lives>i:
        available_letters = get_available_letters(letters_guessed)
        print "Available letters: " + str(available_letters)
        guess = raw_input("Please guess a letter: ")
        letter = guess.lower()
        lab=len(guess)

        if guess=="hint":
            get_hint(secret_word)
        elif (lab> 1):
            print("Invalid Syntex")
            continue
        if not guess.isalpha() :
            print("Invalid Syntex")
            continue
        if letter in secret_word:
            letters_guessed.append(letter)
            print "Good guess: " + get_guessed_word(secret_word, letters_guessed)
            print ""
            i-=1

            if is_word_guessed(secret_word, letters_guessed) == True:
                print " * * Congratulations, you won! * * "
                print ""
                break
        else:
            remain=remaining_lives-i
            print "Your remain live is : ",remain
            ind=index_of_IMAGES[i]
            img=IMAGES[ind]
            print img
        i+=1

    else:
        print "Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed)
        letters_guessed.append(letter)
        print ""
    
# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
import sys
# def get feedback
# def get greens
# get yellows
# get bads
# filter_greens
# filter_yellows
# filter_yellow_order
# filter_bad_letters


def load():
    f = open('wordBank.txt','r')
    return f.read().split('\n')

def get_greens(guess_no,guess):
    if(guess_no == 0): green_string = input(f"My first guess is {guess}, which letters are green? ")    
    else: green_string = input(f"My next guess is {guess} which letters are green? ")

    green_letters = {} 
    green_idx = input("what are the indexes of those letters respectively? (Starting at 0) ")
    try: 
        for (i,j) in zip(green_string,green_idx):
            green_letters[i] = int(j)
    except:
        try:
            green_letters[green_string] = int(green_idx)
        except: 
            green_letters[green_string] = green_idx
    
    return green_letters
        
def get_yellows(): 
    yellow_letters = input(f"which letters are yellow? ")
    return yellow_letters

def get_bad_letters(guess,green_letters,yellow_letters,bad_letters):    
    for i in green_letters.keys():
            guess = guess.replace(i,'')
    for i in yellow_letters:
        guess = guess.replace(i,'')
    for i in guess:
        bad_letters.append(i)


    return bad_letters
    
   


def filter_greens(green_letters,word_bank):
    temp = set(word_bank)
    for word in temp:
        success = 0
        for char in green_letters.keys():
            #print(word,char,word[green_letters[char]])
            if(char == word[green_letters[char]]):
                success += 1
            else: pass
        #print(word, success,len(green_letters.keys()))
        if(success != len(green_letters.keys())):
            word_bank.remove(word)
        else: continue
    return word_bank

def filter_yellows(green_bank,yellow_letters):
    new_bank = []
    for word in green_bank:
        temp = word
        success = 0
        for char in yellow_letters:
            if(char in temp):
                success += 1
                temp = temp.replace(char,'',1)
            else: break
            if(success == len(yellow_letters) and word not in new_bank):
                new_bank.append(word)
            else: continue
    if(new_bank == []): new_bank = green_bank
    return new_bank


# def filter_yellows(word_bank,yellow_letters):
#     new_bank = []
#     temp_word_bank = set(word_bank)
#     for word in temp_word_bank:
#         success = 0
#         temp_word = word
#         for char in yellow_letters:
#             if(char in temp_word):
#                 success += 1
#                 temp_word = temp_word.replace(char,'',1)
#             else: break
#         if(success != len(yellow_letters)):
#                 new_bank.remove(word)
#         else: continue
#     #if(new_bank == []): new_bank = green_bank
#     return new_bank

def filter_bad_letters(new_bank,bad_letters):
    temp = set(new_bank)
    for word in temp:
        for bad_letter in bad_letters:
            if(bad_letter in word):
                new_bank.remove(word)
                break
    return new_bank
    
def filter_yellow_position(yellow_letters,green_letters,guess,new_bank):
    #prevent green letters from mistakenly being yellow letters
    temp_guess = guess
    for green_char in green_letters.keys():
        for yellow_char in yellow_letters:
            if(green_char == yellow_char):
                temp_guess = guess.replace(green_char,' ',1)
    
    yellow_obj = {}
    try:
        for i in yellow_letters:
            yellow_obj[i] = guess.index(i)
    except:
        yellow_obj[yellow_letters] = (temp_guess.index(yellow_letters))


    temp = set(new_bank)
    for word in temp:
        for char in yellow_obj.keys():
            if(char == word[yellow_obj[i]]):
                try:
                    print("here", word)
                    new_bank.remove(word)
                    break
                except:
                    print(word)
    return new_bank
    



def main():
    bad_letters = []
    word_bank = load()
    guess = "ready"
    for i in range(7):
       greens = get_greens(i,guess)
       yellows = get_yellows()
       bad_letters = get_bad_letters(guess,greens,yellows,bad_letters)
       green_bank = filter_greens(greens,word_bank)
       yellow_bank = filter_yellows(green_bank,yellows)
       bad_bank = filter_bad_letters(yellow_bank,bad_letters)
       #print(bad_bank)
       new_bank = filter_yellow_position(yellows,greens,guess,bad_bank)
       print(new_bank)
       if(new_bank==[]): 
           new_bank = load()
       guess = new_bank[0]

       
main()
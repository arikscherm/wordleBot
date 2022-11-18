def load():
    f = open('wordBank.txt','r')
    return f.read().split('\n')


def get_letter_index_mapping(color): # Ask for matching letters and indexes, and returns a mapping of letter to index
    letters = list(input(f"Which letters are {color}? "))
    indexes = input("what are the indexes of those letters respectively? (Starting at 0) ")
    letter_to_index = {} 
    for letter, index in zip(letters, indexes):
        letter_to_index[letter] = index

    return letter_to_index


def get_word_object(greens,yellows,grays,word_object):
    for letter,index in greens.items():
        word_object[index]["good"] = letter
    for letter,index in yellows.items():
        word_object[index]["bad"].append(letter)
    for letter,index in grays.items():
        for i in word_object.keys():
            if(letter != word_object[i]["good"]):
                word_object[i]["bad"].append(letter)
    return word_object


def get_must_haves(greens,yellows,must_haves): 
    #return list(must_haves.update(greens.keys()) + list(yellows.keys()))
    for g in greens.keys():
        must_haves.append(g)
    for y in yellows.keys():
        must_haves.append(y)
    return must_haves


def update_word_bank(word_bank,word_object,must_haves):
    #filter words that dont have all known greens and yellows
    temp_bank = set(word_bank)
    for word in temp_bank: 
        flag = False
        for char in must_haves:
            if char not in word: 
                word_bank.remove(word)
                flag = True
                break     

        #filter words that have wrong chars in green index
        if(flag): continue
        for slot,constraints in word_object.items():
            if word[int(slot)] != constraints["good"] and constraints["good"] != '': 
                word_bank.remove(word)
                break

        #filter words that have yellow in guessed word's index
        #filter words that have any grays
            if word[int(slot)] in constraints["bad"]: 
                word_bank.remove(word)
                break   
    return word_bank
        

def main():
    word_object = {'0': {"good":'',"bad":[]},'1': {"good":'',"bad":[]},'2': {"good":'',"bad":[]},'3': {"good":'',"bad":[]},'4':{"good":'',"bad":[]}}
    must_haves = []
    print("My first guess is ready")
    word_bank = load()
    for i in range(5):
        greens = get_letter_index_mapping("green")
        yellows = get_letter_index_mapping("yellow")
        grays = get_letter_index_mapping("gray")
        word_object = get_word_object(greens,yellows,grays,word_object)
        print(word_object)
        must_haves = get_must_haves(greens,yellows,must_haves)
        word_bank = update_word_bank(word_bank,word_object,must_haves)
        guess = word_bank[0]
        print(word_bank)
        print(f"My next guess is {guess}")
main()
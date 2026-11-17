### prvni projekt ENGETO - textovy analyzer
##zadany text
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
##seznam uzivatelu
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}
#program
pocet_textu = len(TEXTS)
username = input("Username: ")
password = input("Password: ")
oddelovac = "*"*50

if users.get(username) != None and password == users[username]: 
    print(oddelovac)
    print(f"Welcome to the app, {username}.")
    print(f"We have {pocet_textu} texts to be analyzed")
    print(oddelovac)
else:
    print("unregistered user, terminating the program..")
    exit()

choice = input(f"Enter a number btw. 1 and {pocet_textu} to select: ")   
#kontrola na ciselne zadani
if choice.isdigit() :
    choice = int(choice)-1 #zohledneni indexovani od 0
else:
    print("wrong input, terminating the program..")
    exit()
#kontrola na rozsah zadani
if choice < 0 or choice > pocet_textu-1: 
        print("wrong input, terminating the program..")
        exit()

##analyza vybraneho textu
#promenne
wordcount, title_word, upper_word, lower_word, number_word = 0, 0, 0, 0, 0
number_sum = 0

#rozdeleni textu na jednotliva slova a ocisteni o interpunkci
text = [word.strip(".,!?;:") for word in TEXTS[choice].split()]

text_max_len = len(max(text, key=len)) + 1 #nejdelsi slovo v textu +1 index
word_len = [0] * text_max_len #list dle delky slov 

for word in text:
    if word != "":
        wordcount += 1
        word_len[len(word)] += 1 #dle delky slova prictu do listu
        if word.istitle():
            title_word += 1 
        elif word.isupper():
            upper_word += 1
        elif word.islower():
            lower_word += 1
        elif word.isnumeric():
            number_word += 1
            number_sum += int(word)

#vypis informaci
print(f"There are {wordcount} words in the selected text.")
print(f"There are {title_word} titlecase words.")
print(f"There are {upper_word} uppercase words.")
print(f"There are {lower_word} lowercase words.")
print(f"There are {number_word} numeric strings.")
print(f"The sum of all the numbers is {number_sum}.")
print(oddelovac)
print("LEN| ", format("OCCURENCIES".ljust(text_max_len + 10)),"|NR.")
print(oddelovac)
for len in range(1, text_max_len):
    bar = "*" * word_len[len]
    print(f"{len:>3}|{bar.ljust(text_max_len + 13)}|{word_len[len]}")

#konec

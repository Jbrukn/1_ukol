'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jakub Brukner
email: jbrukner@seznam.cz
'''

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
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


users = { "bob": "123",
         "ann": "pass123",
         "mike": "password123",
         "liz": "pass123"
         }

num_delimiters = 30

input_name = input("Zadejte prosím uživatelské jméno: ").strip()

if input_name in users:
    print("Vítej ", input_name , " pokračujeme dále.")
else:
    print("Uživatel se jménem " , input_name , " neexistuje, ukončuji program.")
    exit()

password = input("Zadejte heslo: ").strip()

pocet_pokusu = 3

for i in range(pocet_pokusu-1):
    if password == users[input_name]: break
    print("Chybne heslo, zadejte znovu.")
    print("Zbyva pokusu:", pocet_pokusu-i-1)
    password = input().strip()
else:
    print("Bylo " , pocet_pokusu , "x špatně zadané heslo. Ukončuji program.")
    exit()

print("-"*num_delimiters)
print("Dostupných textů k analýze: ", len(TEXTS))

for i in range(len(TEXTS)):
    vybrany_text = TEXTS[i]
    slova_text = vybrany_text.split()
    print("Text č." , i+1)
    for j in range(6):
        print(slova_text[j], end = " ")
    print("...")       

print("-"*num_delimiters)
text_num = input("Vyber číslo textu který chceš analyzovat:").strip()

if text_num.isdigit():
    print("Vybral jsi text č.", text_num)
    text_num = int(text_num)
    if text_num > len(TEXTS) or text_num < 1:
        print("K zadanému číslu není k dispozici žádný text. Program končí.")        
        exit()
else:
    print("Nebylo zadáno číslo, ukončuji program.")
    exit()
print("-"*num_delimiters)

vybrany_text = TEXTS[text_num-1]
slova_text = vybrany_text.split()


pocet_slov_male = 0
pocet_slov_velke = 0
pocet_slov_prvni_velke = 0
pocet_cisel = 0
suma_cisel = 0
max_delka = (len(max(slova_text, key=len)) + 1)
typy_delek = [0] * max_delka

pocet_slov = len(slova_text)

for slovo in slova_text:
    if all(znak.isupper() for znak in slovo):
        pocet_slov_velke += 1              
    if all(znak.islower() for znak in slovo):    
        pocet_slov_male += 1
    if slovo[0].isupper(): 
        pocet_slov_prvni_velke += 1
    if slovo.isdigit(): 
        pocet_cisel += 1
        suma_cisel += float(slovo)        
    delka_slova = len(slovo)
    #print(delka_slova, "delka je  " ,slovo)
    typy_delek[delka_slova] += 1
        
print("Celkový počet slov je: ",pocet_slov)
print("Slov začínajícím velkým písmenem: ",pocet_slov_prvni_velke)
print("Slov napsanými velkými písmeny: ",pocet_slov_velke)
print("Slov napsanými malými písmeny: ",pocet_slov_male)
print("Počet čísel v textu: ",pocet_cisel)
print("Součet čísel: ",round(suma_cisel))
print("-"*num_delimiters)


print(f'{"Delka":5}{"|"}{"Vyskyt":<16}{"|"}{"Pocet"}')
for znak in range(len(typy_delek)):    
    if typy_delek[znak] != 0:        
        print(f'{znak:5}{"|"}{"*"*typy_delek[znak]:<16}{"|"}{typy_delek[znak]}')
        # print(znak,"|","*"*pokus[znak], pokus[znak])

print("Děkujeme že jste si nás vybrali pro analýzu textu a přejeme hezký zbytek dne!")
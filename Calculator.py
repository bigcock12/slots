# Slots Game #
import pygame
import time
import random



Diamonds = 0
display = [  ]
symbols = ["7", "Bar" , "Diamond"]

cash = 100



def main():
    
    for i in range(3):
        symbol = random.randint(0,100)
        if symbol >= 0 and symbol <= 40:
            choosen_symbol = symbols[0]   
        if symbol >=40 and symbol <=80:
            choosen_symbol = symbols[1]
        if symbol >= 80:
            choosen_symbol = symbols[2]

        display.append(choosen_symbol)
        print(display)

def output():
    




def berrechnung(Diamonds, cash , display):
    time.sleep(2)
    main()
    for i in range(3):
        if display[i] == "Diamond":
            Diamonds += 1 
    if Diamonds != 3:
        if Diamonds == 1:
            print("Ein Dia Stark")
            cash += 5 
        if Diamonds == 2 :
            print("Zwei Dias Stark")
            cash += 20

    if ((display[0] == "7") and (display[1] == "7" ) and (display[2] == "7")):
        print("Starker Zug!")
        cash += 250
        
    if ((display[0] == "Bar") and (display[1] == "Bar" ) and (display[2] == "Bar")):
        print("Full Bar, da geht aber noch mehr!")
        cash += 150
        
    if ((display[0] == "Diamond") and (display[1] == "Diamond" ) and (display[2] == "Diamond")):
        print("hauptgewinn!!!")
        cash += 500   
    else:
        cash -= 5

    print(cash)
    Diamonds = 0
    display = []


berrechnung(Diamonds, cash , display)
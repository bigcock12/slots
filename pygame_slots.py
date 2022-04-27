import time
from pygame import mixer
import random 
import pygame
import sys
mixer.init()
pygame.init()
win = False
cash = 100

pygame_icon = pygame.image.load('icon.png')
pygame.display.set_icon(pygame_icon)

first_slot = pygame.image.load("white.png")
second_slot = pygame.image.load("white.png")
third_slot = pygame.image.load("white.png")

symbols = ["7", "Cherrys", "Melon" , "peach" , "banana"]
display = []
screen = pygame.display.set_mode((600,400))
font = pygame.font.SysFont('Comic Sans MS', 20)
clock = pygame.time.Clock()
pygame.display.set_caption("Slots by Philipp and Jan :D")
def textObjekt(text, font):
    textFlaeche = font.render(text, True, (0,0,0))
    return textFlaeche,textFlaeche.get_rect()
 
keys = pygame.key.get_pressed()
aktiv = False
spin = False
def button(bx,by,nachricht,laenge,hoehe,farbe_normal,farbe_aktiv,randDicke):
    global aktiv
    global spin
    if maus[0] > bx and maus[0] < bx+laenge and maus[1] > by and maus[1] < by+hoehe:
        pygame.draw.rect(screen, farbe_aktiv, (bx,by,laenge,hoehe,))
        if klick[0] == 1 and aktiv == False:
            aktiv = True
            if nachricht == "START":
                spin = True
                
                
            elif nachricht == "QUIT":
                sys.exit()
        if klick[0] == 0:
            aktiv = False
    else:
        pygame.draw.rect(screen, farbe_normal, (bx,by,laenge,hoehe))
    pygame.draw.rect(screen, (0,0,0), (bx,by,laenge,hoehe),randDicke)
    textGrund,textKasten = textObjekt(nachricht,font)
    textKasten.center = ((bx+(laenge/2)),(by+(hoehe/2)))
    screen.blit(textGrund, textKasten)

def output():
        global first_slot
        global second_slot
        global third_slot    
        for i in range(1,4):
                symbol = random.randint(0,200)
                if symbol <= 60:
                    choosen_symbol = symbols[0]
                if symbol>=60 and symbol <=100:
                    choosen_symbol = symbols[1]
                if symbol >= 100 and symbol <= 140:
                    choosen_symbol = symbols[2]   
                if symbol >=140 and symbol <=180:
                    choosen_symbol = symbols[3]
                if symbol >= 180:
                    choosen_symbol = symbols[4]
                display.append(choosen_symbol)
            
                if i == 1:
                    if choosen_symbol == "7":
                        first_slot = pygame.image.load("7_slots.jpg")
                    if choosen_symbol == "Cherrys":
                        first_slot = pygame.image.load("Cherrys.jpg")
                    if choosen_symbol == "Melon":
                        first_slot = pygame.image.load("melon.jpg")
                    if choosen_symbol == "peach":
                        first_slot = pygame.image.load("peach.jpg")
                    if choosen_symbol == "banana":
                        first_slot = pygame.image.load("banana.jpg")
                if i == 2:
                    if choosen_symbol == "7":
                        second_slot = pygame.image.load("7_slots.jpg")
                    if choosen_symbol == "Cherrys":
                        second_slot = pygame.image.load("Cherrys.jpg")
                    if choosen_symbol == "Melon":
                        second_slot = pygame.image.load("melon.jpg")
                    if choosen_symbol == "peach":
                        second_slot = pygame.image.load("peach.jpg")
                    if choosen_symbol == "banana":
                        second_slot = pygame.image.load("banana.jpg")
                if i == 3:
                    if choosen_symbol == "7":
                        third_slot = pygame.image.load("7_slots.jpg")
                    if choosen_symbol == "Cherrys":
                        third_slot = pygame.image.load("Cherrys.jpg")
                    if choosen_symbol == "Melon":
                        third_slot = pygame.image.load("melon.jpg")
                    if choosen_symbol == "peach":
                        third_slot = pygame.image.load("peach.jpg")
                    if choosen_symbol == "banana":
                        third_slot = pygame.image.load("banana.jpg")

                
          

def berechnung():    
    global cash
    global win
    win = False
    if ((display[0] == "7") and (display[1] == "7" ) and (display[2] == "7")):
        win = True
        cash += 250

    if ((display[0] == "Cherrys") and (display[1] == "Cherrys" ) and (display[2] == "Cherrys")):
        win = True
        cash += 150
    
    if ((display[0] == "Melon") and (display[1] == "Melon" ) and (display[2] == "Melon")):
        win = True
        cash += 150

    if ((display[0] == "peach") and (display[1] == "peach" ) and (display[2] == "peach")):
        win = True
        cash += 150
    
    if ((display[0] == "banana") and (display[1] == "banana" ) and (display[2] == "banana")):
        win = True
        cash += 150
    
    cash -= 5
    for i in range(-150,105):  
        screen.blit(first_slot, (50,i))   
        screen.blit(second_slot, (250,i))
        screen.blit(third_slot, (450,i))       
        button(0,0,"SLOTS",600,50,(0,150 + i,150 + i),(0,150 + i,150 + i),1,)
        pygame.time.wait(3)
        pygame.display.flip()
    pygame.display.flip()


    
    
    
    

go = True
while go:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spin = True  
    
        
    
    
    screen.fill((255,255,255))
    maus = pygame.mouse.get_pos()
    klick = pygame.mouse.get_pressed()
    
    

        
        
   
    button(150,340,"QUIT",120,60,(150,0,0),(255,0,0),1,)
    button(350,340,"START",120,60,(0,150,0),(0,255,0),1,)
    button(10,300,"cash: "+ str(cash),100,60,(0,139,139),(0,139,139),1,)
    
    if spin == True:
        
        mixer.music.load("spin_sound.ogg")
        mixer.music.set_volume(0.3)
        mixer.music.play()

        
        output()
        berechnung()
        
        mixer.music.load("click.ogg")
        mixer.music.set_volume(0.1)
        mixer.music.play()

        
        
       
        
        spin = False
        pygame.display.flip()
        print(display)
    
        if win == True:
            mixer.music.load("win.mp3")  
            mixer.music.set_volume(1)
            mixer.music.play()  
            
    if win == True:
        for i in range(100):
            button(0,0,"WIN",600,50,(139 + i ,0,139),(139 + i,0,139),1,)
    else:
        button(0,0,"SLOTS",600,50,(0,250,250),(0,250,250),1,)

    screen.blit(first_slot, (50,100)) 
    screen.blit(second_slot, (250,100))
    screen.blit(third_slot, (450,100))
    
    
    display = []
    pygame.display.flip()
    
    
    

    
    
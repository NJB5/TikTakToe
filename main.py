#Import nötiger Bibliotheken
import pygame
import sys

#Starte Pygame
pygame.init()

#Player
X = pygame.image.load("image/X.png")
O = pygame.image.load("image/O.png")
X = pygame.transform.scale(X, (30, 30))
O = pygame.transform.scale(O, (30, 30))

# Farben definieren r, g, b
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)


#Spielfeld
screen = pygame.display.set_mode((300, 300))
screen.blit(black, (0, 0))

#Game 
print("Herzlich wilkommen bei TikTakToe")
player = int(input("Wie viele Spieler seid ihr? 1/2"))




while game == true:
  if player == 1:
    print("Du spiels allein gegen den Computer!")
  if player == 2:
    print("Ihr spielt zu zweit!")

      
    # Programm beenden wenn x gedrückt
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit()

    # Mausposition mx = x-Pos ...
    mx, my = pygame.mouse.get_pos()

    # Steuert die Spielfigur per Maus
    if pygame.mouse.get_pressed()[0]== True:         
      x = mx - 35
      y = my - 35


    # Anzeigen der Bilder
    screen.blit(bg, (0, 0))
    screen.blit(santa, (x, y))

    # Kreise oder Rechtecke laden
    pygame.draw.circle(screen, white, (150, 90), 30)
    #screen.fill((0,0,0))
    #pygame.draw.rect(screen, red, (x,y, 20, 30))

    # am ende der Schleife einmal updaten
    pygame.display.update()

    clock.tick(60)
    #print(clock.get_fps())


#Import nötiger Bibliotheken
import pygame
import sys

#Starte Pygame
pygame.init()

#Player
XO = ""

# Farben definieren r, g, b
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)


# Spieler laden
circle = pygame.image.load("images/Santa.png")

# Skaliere Figur Bild auf 70 70
santa = pygame.transform.scale(santa, (70, 70))

# Gameloop - Endlosschleife
while True:

    # [(a, 0), (b, 0), (up, 0), (space, 1)]
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= speed
    elif pressed[pygame.K_DOWN]:
        y += speed
    elif pressed[pygame.K_LEFT]:
        x -= speed
    elif pressed[pygame.K_RIGHT]:
        x += speed
    elif pressed[pygame.K_SPACE]:
        y -= 10
      
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


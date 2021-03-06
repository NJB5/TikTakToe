#Bibliotheken importieren
import pygame
import sys

# starte pygame
pygame.init()

# legt eine Uhr fest
clock = pygame.time.Clock()
# lädt das Bild in die Variable bg
bg = pygame.image.load("Bilder/Weihnachten.jpg")
# scaliert hintergrund auf Größe 300, 300
bg = pygame.transform.scale(bg, (400, 400))
# Größe des Fenster definieren
screen = pygame.display.set_mode((400, 400))

# Farben definieren r, g, b
yellow = (255, 210, 0)
red = (255, 0, 0)
white = (255, 255, 255)

# Werte für Spielfigur, x, y = Kooridinaten, speed = Geschwindigkeit
x = 200
y = 200
speed = 3

# Rechteck erstellen
rectangle = pygame.Rect(x, y, 20, 30)

# Spieler laden
playerOne = pygame.image.load("images/X.png")
playerTwo = pygame.image.load("images/O.png")

# Skaliert Spieler auf 25 25
playerOne = pygame.transform.scale(playerOne, (25, 25))
playerTwo = pygame.transform.scale(playerTwo, (25, 25))

# Gameloop - Endlosschleife
while True:      
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


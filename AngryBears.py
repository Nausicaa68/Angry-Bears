import pygame
import sys
import pygame.mixer
from pygame.locals import *
import math
import os
from random import *
import time

# images
# image_ours = "images/ours.png"   #vieux skin
image_fond = "images/fond_marin.jpg"
image_ours = "images/sprite2ours.png"
image_ours2 = "images/ours.png"
image_ours3 = "images/sprite1oursgrizzly.png"
image_ours4 = "images/sprite1ourspanda.png"
image_ours5 = "images/sprite1ourssupermode.png"
image_ours6 = "images/sprite1ourssamurai.png"
image_orque = "images/sprite1orque.png"
image_poisson = "images/poisson.png"
image_filet = "images/spritefilet.png"
image_rocher1 = "images/rocher1.png"
image_rocher2 = "images/rocher2.png"
image_rocher3 = "images/rocher3.png"
image_rocher4 = "images/rocher4.png"
image_fleche1 = "images/fleche1.png"
image_fleche2 = "images/fleche2.png"

# Variable skin
skin_choisi = [1]
achat = [1]
# achat skin
skin2 = [1]
skin2[0] = False
skin3 = [1]
skin3[0] = False
skin4 = [1]
skin4[0] = False
skin5 = [1]
skin5[0] = False

# music
pygame.mixer.init()
# pour charger un son que l'on va déclencher lors de la nage ou lorsqu'on mange un poisson, touche un orque
swimmingsound = pygame.mixer.Sound("pygame_music/waterplotch.wav")
#obligatoirement .wav
swimmingsound.set_volume(0.01)  # pour gerer le son
# puis lors de l'appel on fait nom.play()
swallow = pygame.mixer.Sound("pygame_music/swallow.wav")
swallow.set_volume(0.09)

music = pygame.mixer.music.load("pygame_music/healing_water.mp3")   #musique de fond peut être mp3 ou .wav
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)  # le -1 permet de jouer la musique en boucle

# couleur
RED = (255, 0, 0)


def read_score():
    fichier = open("score.txt", "r")

    liste = []
    for line in fichier:
        try:
            liste.append(int(line))
        except ValueError:
            word = ""
            for i in range(len(line)-1):
                word += line[i]

            liste.append(word)

    fichier.close()
    return liste


def fonction_menu(skin_choisi, achat, skin2, skin3, skin4, skin5):

    pygame.init()

    # create the screen
    # fond noir
    N = (0, 0, 0)  # couleur noir
    R = (255, 0, 0)  # couleur rouge
    B = (9, 11, 69)  # couleur bleu
    V = (73, 28, 69)  # couleur violet
    win_resolution = (1200, 700)
    win = pygame.display.set_mode(win_resolution)
    # Background

    background = pygame.image.load(image_fond).convert()
    '''
    # Sound

    mixer.music.load("background.wav")
    mixer.music.play(-1)

    '''
    # Caption and Icon
    pygame.display.set_caption("Angry Bears")

    # icon = pygame.image.load('images/icone_ours.jpg')
    # pygame.display.set_icon(icon)

    # conversion de toutes les images
    ours = pygame.image.load(image_ours).convert_alpha()
    ours2 = pygame.image.load(image_ours2).convert_alpha()
    ours3 = pygame.image.load(image_ours3).convert_alpha()
    ours4 = pygame.image.load(image_ours4).convert_alpha()
    ours5 = pygame.image.load(image_ours5).convert_alpha()
    ours6 = pygame.image.load(image_ours6).convert_alpha()
    fleche1 = pygame.image.load(image_fleche1).convert_alpha()
    fleche2 = pygame.image.load(image_fleche2).convert_alpha()

    # conversion des polices
    Texty1 = pygame.font.SysFont("arial", 40)
    Texty2 = pygame.font.SysFont("arial", 20)
    Texty3 = pygame.font.SysFont("arial", 30)
    Texty_bright = pygame.font.SysFont("arial", 58)
    # changement de taille pour le titre
    Text = pygame.font.SysFont("broadway", 70)

    T_jouer = Texty1
    T_aide = Texty1
    T_quit = Texty1

    # score et points
    score = read_score()
    i = score[0]
    j = score[1]
    k = score[2]
    l = score[3]  # attention, str

    option = 0  # position initiale joueur dans le menu
    skin = 0  # choix initiale du skin
    skin_choisi = [1]

    run = True

    while run == True:

        for event in pygame.event.get():
            # navigation dans le menu
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    option = option+1
                if event.key == K_UP:
                    option = option-1
                if event.key == K_RIGHT:
                    skin = skin+1
                if event.key == K_LEFT:
                    skin = skin-1
                if event.key == K_SPACE and option == 2:
                    pygame.quit()
                    sys.exit()
                if event.key == K_SPACE and option == 1:
                    fonction_aide()
                if event.key == K_SPACE and option == 0:
                    fonction_jeu(skin_choisi, achat)

        # position du curseur
        if option == -1:
            option = 0
        if option == 0:
            T_jouer = Texty_bright
            T_aide = Texty1
            T_quit = Texty1
        if option == 1:
            T_aide = Texty_bright
            T_jouer = Texty1
            T_quit = Texty1
        if option == 2:
            T_quit = Texty_bright
            T_aide = Texty1
            T_jouer = Texty1
        if option == 3:
            option = 2

        # choix du skin
        if skin == -1:
            skin = 0
        if skin == 6:
            skin = 5

        # Boutique
        if skin == 2 and skin2[0] == False:
            prix = Texty2.render("20 poissons", 0, (255, 0, 0))
        if skin == 3 and skin3[0] == False:
            prix = Texty2.render("50 poissons", 0, (255, 0, 0))
        if skin == 4 and skin4[0] == False:
            prix = Texty2.render("100 poissons", 0, (255, 0, 0))
        if skin == 5 and skin5[0] == False:
            prix = Texty2.render("200 poissons", 0, (255, 0, 0))

        # affichage des ecritures avec leur couleur
        score_base = Texty1.render("High score = "+str(i) + ' m', 0, V)
        points_base = Texty1.render("poisson(s) = "+str(j), 0, V)
        nom_joueur = Texty1.render(str(l), 0, V)
        nom = Text.render("ANGRY BEARS ", 0, B)
        jouer = T_jouer.render("jouer", 0, R)
        aide = T_aide.render("aide", 0, R)
        quitter = T_quit.render("quitter ", 0, R)
        informations = Texty2.render(
            "réalisé par J. Grelaud, J. Hassoun, A. Rossignol, J.Thavarasa, G.Dumas", 0, (0, 0, 255))
        informations1 = Texty2.render(
            "musique: healing_water ", 0, (0, 0, 255))
        boutique = Texty3.render(
            "Press E pour acheter le skin ", 0, (253, 51, 2))

        # afficher les ecritures

        win.blit(background, (0, 0))
        if skin == 0:
            win.blit(ours, (120, 350))
            skin_choisi[0] = 0
        if skin == 1:
            win.blit(ours2, (120, 350))
            skin_choisi[0] = 1
        if skin == 2:
            win.blit(ours3, (120, 350))
            if skin2[0] == False:
                win.blit(prix, (120, 440))
                win.blit(boutique, (60, 465))
                if event.type == KEYDOWN:
                    if event.key == K_e and 20 <= j:
                        j = j-20
                        achat[0] = 20
                        skin_choisi[0] = 2
                        skin2[0] = True
            if skin2[0] == True:
                skin_choisi[0] = 2
        if skin == 3:
            win.blit(ours4, (120, 350))
            if skin3[0] == False:
                win.blit(prix, (120, 440))
                win.blit(boutique, (60, 465))
                if event.type == KEYDOWN:
                    if event.key == K_e and 50 <= j:
                        j = j-50
                        achat[0] = 50
                        skin_choisi[0] = 3
                        skin3[0] = True
            if skin3[0] == True:
                skin_choisi[0] = 3
        if skin == 4:
            win.blit(ours5, (100, 280))
            if skin4[0] == False:
                win.blit(prix, (120, 440))
                win.blit(boutique, (60, 465))
                if event.type == KEYDOWN:
                    if event.key == K_e and 100 <= j:
                        j = j-100
                        achat[0] = 100
                        skin_choisi[0] = 4
                        skin4[0] = True
            if skin4[0] == True:
                skin_choisi[0] = 4
        if skin == 5:
            win.blit(ours6, (120, 350))
            if skin5[0] == False:
                win.blit(prix, (120, 440))
                win.blit(boutique, (60, 465))
                if event.type == KEYDOWN:
                    if event.key == K_e and 200 <= j:
                        j = j-200
                        achat[0] = 200
                        skin_choisi[0] = 5
                        skin5[0] = True
            if skin5[0] == True:
                skin_choisi[0] = 5
        win.blit(score_base, (20, 20))
        win.blit(points_base, (950, 20))
        win.blit(nom_joueur, (510, 20))
        win.blit(fleche1, (65, 365))
        win.blit(fleche2, (245, 365))
        win.blit(nom, (340, 120))
        win.blit(jouer, (550, 260))
        win.blit(aide, (550, 340))
        win.blit(quitter, (550, 420))
        win.blit(informations, (30, 650))
        win.blit(informations1, (950, 650))

        pygame.display.update()


def fonction_aide():
    import pygame
    # Appuyer sur aide ouvre une fenetre qui donne des indications au joueur

    pygame.init()
    X = 1200
    Y = 700
    ecran = pygame.display.set_mode((X, Y))
    black = (0, 0, 0)
    continuer = True

    # images
    image_fond = "images/fond_marin.jpg"

    background = pygame.image.load(image_fond).convert()

    # Caption and Icon
    pygame.display.set_caption("Angry Bears")

    # icon = pygame.image.load('images/icone_ours.jpg')
    # pygame.display.set_icon(icon)

    font = pygame.font.SysFont("arial", 40)
    text1 = font.render("Aide sur le jeu :", True, black, None)
    textRect1 = text1.get_rect()
    textRect1.center = (X // 2, Y // 10)

    font2 = pygame.font.SysFont("arial", 25)
    text2 = font2.render(
        "Utilisez la barre espace pour nager vers le haut, la gravité vous fera redescendre quand vous n'appuierez pas", True, black, None)
    textRect2 = text2.get_rect()
    textRect2.center = (X // 2, 200)

    font3 = pygame.font.SysFont("arial", 25)
    text3 = font3.render(
        "Vous devez éviter les orques, rochers et les filets qui arrivent à droite et récupérer les poissons", True, black, None)
    textRect3 = text3.get_rect()
    textRect3.center = (X // 2, 250)

    font4 = pygame.font.SysFont("arial", 25)
    text4 = font4.render(
        "Les poissons collectés peuvent être dépensés dans de nouveaux cosmétiques pour l'ours, à gauche du menu", True, black, None)
    textRect4 = text4.get_rect()
    textRect4.center = (X // 2, 300)

    font5 = pygame.font.SysFont("arial", 25)
    text5 = font5.render(
        "Votre score est affiché à gauche du menu", True, black, None)
    textRect5 = text5.get_rect()
    textRect5.center = (X // 2, 350)

    font6 = pygame.font.SysFont("arial", 25)
    text6 = font6.render(
        "Appuyez sur une touche pour revenir au jeu", True, black, None)
    textRect6 = text6.get_rect()
    textRect6.center = (X // 2, 550)

    while continuer:

        ecran.blit(background, (0, 0))
        ecran.blit(text1, textRect1)
        ecran.blit(text2, textRect2)
        ecran.blit(text3, textRect3)
        ecran.blit(text4, textRect4)
        ecran.blit(text5, textRect5)
        ecran.blit(text6, textRect6)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                continuer = False
            pygame.display.update()

    fonction_menu(skin_choisi, achat, skin2, skin3, skin4, skin5)


def fonction_jeu(skin_choisi, achat):

    def write_score(Score, nbPoissons, skinPossede, name, achat):
        liste = []
        liste = read_score()

        fichier = open("score.txt", "w")

        if (liste[0] < Score):
            liste[0] = Score
        liste[1] = liste[1] + nbPoissons - achat[0]
        liste[2] = skinPossede
        liste[3] = name

        for i in range(4):
            fichier.write(str(liste[i]))
            fichier.write("\n")

        achat[0] = 0

        fichier.close()

    def menu_pause():  # echap pour mettre en pause

        pygame.init()

        os.environ['SDL_VIDEO_WINDOW_POS'] = "200,50"
        win_resolution = (1200, 700)
        win = pygame.display.set_mode(win_resolution)
        paused = True

        N = (0, 0, 0)  # couleur noir
        R = (255, 0, 0)  # couleur rouge
        B = (9, 11, 69)  # couleur bleu

        # position initiale curseur
        option = 0

        fond = pygame.image.load(image_fond).convert()

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and option == 0:  # pour reprendre
                        paused = False
                    elif event.key == pygame.K_SPACE and option == 1:
                        fonction_aide()
                    elif event.key == pygame.K_SPACE and option == 2:
                        fonction_menu(skin_choisi, achat, skin2,
                                      skin3, skin4, skin5)
                    elif event.key == pygame.K_DOWN:
                        option = option+1
                    elif event.key == pygame.K_UP:
                        option = option-1

            # Typographie
            Texty1 = pygame.font.SysFont("arial", 100)
            Texty2 = pygame.font.SysFont("arial", 40)
            Texty_bright = pygame.font.SysFont("arial", 60)

            T_reprendre = Texty2
            T_aide = Texty2
            T_menu = Texty2

            # position du curseur
            if option == -1:
                option = 0
            if option == 0:
                T_reprendre = Texty_bright
                T_aide = Texty2
                T_menu = Texty2
            if option == 1:
                T_aide = Texty_bright
                T_reprendre = Texty2
                T_menu = Texty2
            if option == 2:
                T_menu = Texty_bright
                T_aide = Texty2
                T_reprendre = Texty2
            if option == 3:
                option = 2

            pause = Texty1.render("PAUSE ", 0, B)
            reprendre = T_reprendre.render("Reprendre ", 0, (255, 0, 0))
            aide = T_aide.render("Aide ", 0, (255, 0, 0))
            menu = T_menu.render("Menu ", 0, (255, 0, 0))

            # Affichage
            win.blit(fond, (0, 0))
            win.blit(pause, (470, 80))
            win.blit(reprendre, (505, 240))
            win.blit(aide, (545, 320))
            win.blit(menu, (535, 400))

            pygame.display.update()

    def events(pausetime):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif (event.type == KEYDOWN and event.key == K_ESCAPE):
                pausetime[0] = time.time()
                menu_pause()
                pausetime[1] = time.time()

    def keyPressed(inputKey):
        keysPressed = pygame.key.get_pressed()
        if keysPressed[inputKey]:
            return True
        else:
            return False

    def hitbox_ours(posplayer):
        rectangle_ours = pygame.Rect(posplayer[0]+5, posplayer[1], 112, 75)
        return rectangle_ours

    def hitbox_super_ours(posplayer):
        # il faut l'appeler quand c le skin super ours le numero 5
        rectangle_ours = pygame.Rect(posplayer[0]+45, posplayer[1]+35, 95, 85)
        return rectangle_ours

    def hitbox_classic_ours(posplayer):
        # il faut l'appeler quand c le 2eme skin ours
        rectangle_ours = pygame.Rect(posplayer[0]+10, posplayer[1], 95, 65)
        return rectangle_ours

    def hitbox_poisson(pospoisson):
        rectangle_poissson = pygame.Rect(
            pospoisson[0]+20, pospoisson[1]+15, 76, 35)
        return rectangle_poissson

    def hitbox_orque(posorque):
        rectangle_orque = pygame.Rect(posorque[0]+5, posorque[1], 130, 87)
        return rectangle_orque

    def hitbox_rocher1(posrocher1):
        rectangle_rocher1 = pygame.Rect(
            posrocher1[0]+41, posrocher1[1]+10, 160, 110)
        return rectangle_rocher1

    def hitbox_rocher2(posrocher2):
        rectangle_rocher2 = pygame.Rect(
            posrocher2[0]+61, posrocher2[1], 145, 115)
        return rectangle_rocher2

    def hitbox_rocher3(posrocher3):
        rectangle_rocher3 = pygame.Rect(
            posrocher3[0]+28, posrocher3[1]+15, 180, 125)
        return rectangle_rocher3

    def hitbox_rocher4(posrocher4):
        rectangle_rocher4 = pygame.Rect(
            posrocher4[0]+20, posrocher4[1]+5, 168, 110)
        return rectangle_rocher4

    def hitbox_filet(posfilet):
        rectangle_filet = pygame.Rect(posfilet[0]+88, posfilet[1]+25, 90, 115)
        return rectangle_filet

    def collision_orque_ours(rectangle_ours, rectangle_orque):
        collision = rectangle_ours.colliderect(rectangle_orque)
        return collision

    def collision_poisson_ours(rectangle_ours, rectangle_poisson):
        collision = rectangle_ours.colliderect(rectangle_poisson)
        return collision

    def collision_ours_filet(rectangle_ours, rectangle_filet):
        collision = rectangle_ours.colliderect(rectangle_filet)
        return collision

    def collision_ours_rocher(rectangle_ours, rectangle_rocher):
        collision = rectangle_ours.colliderect(rectangle_rocher)
        return collision

    def fenetre_game_over(nbPoisson, distance, skinPossede, name):
        # fenetre game_over ramène au menu

        pygame.init()
        X = 1200
        Y = 700
        ecran = pygame.display.set_mode((X, Y))
        black = (0, 0, 0)
        continuer = True

        # images
        image_fond = "images/fond_marin.jpg"
        image_gameover = "images/gameover.png"
        background = pygame.image.load(image_fond).convert()
        gameover = pygame.image.load(image_gameover).convert_alpha()

        # Caption and Icon
        pygame.display.set_caption("Angry Bears")

        # icon = pygame.image.load('images/icone_ours.jpg')
        # pygame.display.set_icon(icon)

        # score et points
        write_score(distance, nbPoisson, skinPossede, name, achat)

        Texty1 = pygame.font.SysFont("arial", 40)  # police
        V = (73, 28, 69)  # couleur violet

        score_distance = Texty1.render("score = "+str(distance) + ' m', 0, V)
        nb_poissons = Texty1.render("poisson(s) = "+str(nbPoisson), 0, V)

        font2 = pygame.font.SysFont("arial", 25)
        text2 = font2.render(
            "Appuyez sur une touche pour revenir au menu", True, black, None)
        textRect2 = text2.get_rect()
        textRect2.center = (X // 2, 500)

        ecran.blit(background, (0, 0))
        ecran.blit(score_distance, (20, 20))
        ecran.blit(nb_poissons, (950, 20))
        ecran.blit(gameover, (370, 100))
        ecran.blit(text2, textRect2)
        pygame.display.update()

        while continuer:

            ecran.blit(background, (0, 0))
            ecran.blit(score_distance, (20, 20))
            ecran.blit(nb_poissons, (950, 20))
            ecran.blit(gameover, (370, 100))
            ecran.blit(text2, textRect2)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    continuer = False
                pygame.display.update()

        fonction_menu(skin_choisi, achat, skin2, skin3, skin4, skin5)

    W, M = 1200, 700
    HW, HM = W//2, M//2
    AREA = W*M

    # liste des positions
    liste_x_ours = []
    liste_y_ours = []
    liste_x_poisson = []
    liste_y_poisson = []
    liste_x_orque = []
    liste_y_orque = []

    # position de depart de la fenetre par rapport au haut à gauche   centré pour un ecran 17pouces
    os.environ['SDL_VIDEO_WINDOW_POS'] = "200,50"

    pygame.init()
    screen = pygame.display.set_mode((W, M))
    if skin_choisi[0] == 0:
        ours = pygame.image.load(image_ours).convert_alpha()
    if skin_choisi[0] == 1:
        ours = pygame.image.load(image_ours2).convert_alpha()
    if skin_choisi[0] == 2:
        ours = pygame.image.load(image_ours3).convert_alpha()
    if skin_choisi[0] == 3:
        ours = pygame.image.load(image_ours4).convert_alpha()
    if skin_choisi[0] == 4:
        ours = pygame.image.load(image_ours5).convert_alpha()
    if skin_choisi[0] == 5:
        ours = pygame.image.load(image_ours6).convert_alpha()
    posplayer = ours.get_rect()
    posplayer[0] = 100
    posplayer[1] = HM

    # orque
    orque = pygame.image.load(image_orque).convert_alpha()
    posorque = orque.get_rect()
    posorque[0] = 1200
    posorque[1] = randint(0, 640)
    val_rand_orque = randint(60, 580)
    game_over = False

    # poisson
    poisson = pygame.image.load(image_poisson).convert_alpha()
    pospoisson = poisson.get_rect()
    pospoisson[0] = 1300
    pospoisson[1] = randint(0, 640)
    poisson_manger = False

    # filet
    filet = pygame.image.load(image_filet).convert_alpha()
    posfilet = filet.get_rect()
    posfilet[0] = -500
    posfilet[1] = 0

    # rochers
    # rocher1
    rocher1 = pygame.image.load(image_rocher1).convert_alpha()
    posrocher1 = rocher1.get_rect()
    posrocher1[0] = 1300
    posrocher1[1] = 550
    # rocher2
    rocher2 = pygame.image.load(image_rocher2).convert_alpha()
    posrocher2 = rocher2.get_rect()
    posrocher2[0] = 1300
    posrocher2[1] = 550
    # rocher3
    rocher3 = pygame.image.load(image_rocher3).convert_alpha()
    posrocher3 = rocher3.get_rect()
    posrocher3[0] = 1300
    posrocher3[1] = 523
    # rocher4
    rocher4 = pygame.image.load(image_rocher4).convert_alpha()
    posrocher4 = rocher4.get_rect()
    posrocher4[0] = 1300
    posrocher4[1] = 550

    # scores
    score_poisson = 0  # sera le nbr de poissons mangés
    score_distance = 0  # sera la distance parcouru calculée en focntion du temps
    Text_distance = pygame.font.SysFont("arial", 35)
    B = (9, 11, 69)  # couleur bleu
    #distance =  Text_distance.render('Distance : '+str(score_distance) +' m', 1, B)
    #nb_poisson = Text_distance.render('Poissons : '+str(score_poisson), 1, B)

    backgr = pygame.image.load(image_fond).convert()  # chargement du fond
    pygame.key.set_repeat(400, 1)  # pour la repetion de touches
    # pour le scrolling #mesure du temps
    CLOCK = pygame.time.Clock()
    # CLOCK.tick(30)  #pour actualiser le temps selon un certain taux de rafarichissement entre paranthèse minimum 30fps pour que ce soit fluide à l'oeil nu
    # pygame.time.get_ticks()  #le temps en ms
    FPS = 144
    avance = 1
    x_scroll = 0
    selection = False

    # variables pour les scores
    best_score_distance = 0  # bestScore
    score_poisson_total = 0  # nbPoissons
    nb_skins = 2  # skinPossede

    # Temps de pause
    pausetime = [0, 0]

    if ((read_score())[3] == "?"):
        BLUE = (40, 120, 230)
        GREEN = (40, 230, 120)
        font = pygame.font.SysFont('Comic Sans MS,Arial', 24)
        prompt = font.render('Entrez votre nom : ', True, BLUE)
        prompt_rect = prompt.get_rect(center=(HW, HM))

        pseudo = ""
        pseudoAff = font.render(pseudo, True, GREEN)
        pseudoAff_Rect = pseudoAff.get_rect(topleft=prompt_rect.topright)
        creanom = True
        while creanom:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        creanom = False
                    elif event.key == pygame.K_BACKSPACE:
                        pseudo = pseudo[:-1]
                    else:
                        pseudo += event.unicode
                    pseudoAff = font.render(pseudo, True, GREEN)
                    pseudoAff_rect = pseudoAff.get_rect(
                        topleft=prompt_rect.topright)
            screen.fill(0)
            screen.blit(prompt, prompt_rect)
            screen.blit(pseudoAff, pseudoAff_Rect)
            pygame.display.flip()
        write_score(best_score_distance, score_poisson_total,
                    nb_skins, pseudo, achat)
    else:
        pseudo = read_score()[3]

    # initialize the t0 variable, "starting the time"
    t0 = time.time()

    while(0 == 0):
        events(pausetime)
        # screen.blit(backgr,(0,0))
        # x modulo width du background qui vaut 11900
        rel_x = x_scroll % backgr.get_rect().width
        screen.blit(backgr, (rel_x - backgr.get_rect().width, 0))
        if rel_x < W:
            screen.blit(backgr, (rel_x, 0))
        x_scroll -= avance
        # pygame.draw.line(screen, (255, 0, 0), (rel_x, 0), (rel_x, M), 3)   #ligne pour check si la liaison entre les deux images se fait bien
        CLOCK.tick(FPS)
        avance += 0.0001

        cond = keyPressed(K_SPACE)
        if (cond == True) and (posplayer[1] >= 0):
            posplayer[1] = posplayer[1] - 2
            swimmingsound.play()
        if (cond == False) and (posplayer[1] <= 630):
            posplayer[1] = posplayer[1] + 1

        # rectangles/hitbox
        rectangle_orque = hitbox_orque(posorque)

        if(skin_choisi[0] == 4):
            # la hitbox quand c'est le skin du super ours
            rectangle_ours = hitbox_super_ours(posplayer)
        elif(skin_choisi[0] == 1):
            # la hitbox quand c'est le 2eme skin
            rectangle_ours = hitbox_classic_ours(posplayer)
        else:
            rectangle_ours = hitbox_ours(posplayer)

        rectangle_poisson = hitbox_poisson(pospoisson)
        rectangle_rocher1 = hitbox_rocher1(posrocher1)
        rectangle_rocher2 = hitbox_rocher2(posrocher2)
        rectangle_rocher3 = hitbox_rocher3(posrocher3)
        rectangle_rocher4 = hitbox_rocher4(posrocher4)
        rectangle_filet = hitbox_filet(posfilet)
        # pour afficher toutes les hitbox

        '''      
        pygame.draw.rect(screen, RED,rectangle_ours,2)
        pygame.draw.rect(screen, RED,rectangle_orque,2)
        pygame.draw.rect(screen, RED,rectangle_poisson,2)
        pygame.draw.rect(screen, RED,rectangle_rocher1,2)
        pygame.draw.rect(screen, RED,rectangle_rocher2,2)
        pygame.draw.rect(screen, RED,rectangle_rocher3,2)
        pygame.draw.rect(screen, RED,rectangle_rocher4,2)
        pygame.draw.rect(screen, RED,rectangle_filet,2)
        '''

        if pospoisson[0] < 220 and pospoisson[0] > 0:
            poisson_manger = collision_poisson_ours(
                rectangle_ours, rectangle_poisson)

        if pospoisson[0] > -120:
            pospoisson[0] = pospoisson[0]-(2*avance)
        if pospoisson[0] <= -120 or poisson_manger == True:

            pospoisson[0] = 1300
            pospoisson[1] = randint(0, 640)
            if poisson_manger == True:
                swallow.play()
                score_poisson = score_poisson+1
                poisson_manger = False

        if posorque[0] > -500 and posorque[1] <= 640 and posorque[1] >= 0:
            posorque[0] = posorque[0]-(1.5*avance)
            x = posorque[0]
            posorque[1] = (45*math.sin(x/(100))+val_rand_orque)
        elif posorque[0] <= -500:
            posorque[0] = 1300
            val_rand_orque = randint(60, 580)

        if posorque[0] < 220 and posorque[0] > 0:
            game_over = collision_orque_ours(rectangle_ours, rectangle_orque)

            if game_over == True:
                fenetre_game_over(
                    score_poisson, score_distance, nb_skins, pseudo)

        if posfilet[0] > -200:
            posfilet[0] = posfilet[0]-(1)
        if posfilet[0] > -2000:
            posfilet[0] = posfilet[0]-1
        if posfilet[0] <= -2000:
            posfilet[0] = 1300

        if posfilet[0] < 220 and posfilet[0] >= 0:
            attraper = collision_ours_filet(rectangle_ours, rectangle_filet)
            if attraper == True:
                fenetre_game_over(
                    score_poisson, score_distance, nb_skins, pseudo)

        # rochers

        deplacement_rocher = 1
        if avance > deplacement_rocher+1:
            deplacement_rocher += 1

        if selection == False:
            rocher = randint(1, 4)
            selection = True
        if rocher == 1:
            if posrocher1[0] > -200:
                posrocher1[0] -= deplacement_rocher
            if posrocher1[0] <= -200:
                posrocher1[0] = 1300
                selection = False
            # collision avec les rochers
            if posrocher1[0] < 220 and posrocher1[0] > 0:
                collision = collision_ours_rocher(
                    rectangle_ours, rectangle_rocher1)
                if collision == True:
                    fenetre_game_over(
                        score_poisson, score_distance, nb_skins, pseudo)
        elif rocher == 2:
            if posrocher2[0] > -200:
                posrocher2[0] -= deplacement_rocher
            if posrocher2[0] <= -200:
                posrocher2[0] = 1300
                selection = False
            # collision avec les rochers
            if posrocher2[0] < 220 and posrocher2[0] > 0:
                collision = collision_ours_rocher(
                    rectangle_ours, rectangle_rocher2)
                if collision == True:
                    fenetre_game_over(
                        score_poisson, score_distance, nb_skins, pseudo)
        elif rocher == 3:
            if posrocher3[0] > -200:
                posrocher3[0] -= deplacement_rocher
            if posrocher3[0] <= -200:
                posrocher3[0] = 1300
                selection = False
            # collision avec les rochers
            if posrocher3[0] < 220 and posrocher3[0] > 0:
                collision = collision_ours_rocher(
                    rectangle_ours, rectangle_rocher3)
                if collision == True:
                    fenetre_game_over(
                        score_poisson, score_distance, nb_skins, pseudo)
        elif rocher == 4:
            if posrocher4[0] > -200:
                posrocher4[0] -= deplacement_rocher
            if posrocher4[0] <= -200:
                posrocher4[0] = 1300
                selection = False
            # collision avec les rochers
            if posrocher4[0] < 220 and posrocher4[0] > 0:
                collision = collision_ours_rocher(
                    rectangle_ours, rectangle_rocher4)
                if collision == True:
                    fenetre_game_over(
                        score_poisson, score_distance, nb_skins, pseudo)

        # scores
        # score_distance = int((pygame.time.get_ticks()//1000)*avance)  #car c en ms et on multiplie par avance car ca va de plus en plus vite
        t1 = time.time()
        dt = t1 - t0 - (pausetime[1] - pausetime[0])
        score_distance = int(dt)
        distance = Text_distance.render(
            'Distance : '+str(score_distance) + ' m', 1, B)
        nb_poisson = Text_distance.render(
            'Poisson(s) : '+str(score_poisson), 1, B)

        # blit toutes les autres images en plus du background
        screen.blit(rocher1, posrocher1)
        screen.blit(rocher2, posrocher2)
        screen.blit(rocher3, posrocher3)
        screen.blit(rocher4, posrocher4)
        screen.blit(poisson, pospoisson)
        screen.blit(ours, posplayer)
        screen.blit(orque, posorque)
        screen.blit(filet, posfilet)
        screen.blit(distance, [525, 0])
        screen.blit(nb_poisson, [1000, 0])

        pygame.display.flip()
        pygame.display.update()


fonction_menu(skin_choisi, achat, skin2, skin3, skin4, skin5)

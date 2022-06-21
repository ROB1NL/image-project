import pygame

pygame.init()
color_facile = (0, 0, 0)
color_moyen = (0, 0, 0)
color_difficile = (0, 0, 0)
color_diabolique = (0, 0, 0)
taille_ecran_menu = [800 * 0.66, 500 * 0.66]
taille_ecran_menu_difficulte = [800 * 0.66, 800 * 0.66]
taille_ecran_sudoku = [800 * 0.66, 800 * 0.66]
taille_sudoku = [600 * 0.66, 600 * 0.66]
background_color = (0, 38, 38)
taille_police = int(65 * 0.66)
taille_police_titre = int(80 * 0.66)
taille_police_button = int(25 * 0.66)
taille_police_chiffre = int(60 * 0.66)
police_ecriture_menu = pygame.font.SysFont('Didot', taille_police)
police_ecriture_sudoku = pygame.font.SysFont('Comic sans ms', taille_police_titre)
police_ecriture_button = pygame.font.SysFont('Comic sans ms', taille_police_button)
police_ecriture_chiffre = pygame.font.SysFont('Didot', taille_police_chiffre)
violet = (110, 5, 255)
noir = (0, 0, 0)
blanc = (255, 255, 255)
coor_jouer = (80, 80, 150, 80)
rouge = (255, 0, 0)
blue = (0, 0, 255)
vert = (0, 255, 0)
rouge_clair = (255, 100, 100)
gris_clair = (200, 200, 200)
jaune_orange = (255, 255, 120)
grid = [[1, 3, 4, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0]]


class Interface:
    def __init__(self, img_name):  # Constructeur de la classe
        self.img = pygame.image.load(img_name)
        self.taille_img = self.img.get_rect().size
        self.ecran = pygame.display.set_mode(self.taille_img)
        fond = pygame.image.load(img_name).convert(self.ecran)
        self.ecran.blit(fond, (0, 0))


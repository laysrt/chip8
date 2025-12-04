import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720)) # Dimension de l'écran
clock = pygame.time.Clock()
running = True
dt = 0


RADIUS = 40
SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()
FONT_SIZE = 18 # Taille de la police d'écriture
TEXT_COLOR = (255, 255, 255) # Couleur du texte en Blanc
BG_TEXT_COLOR = (50, 50, 50, 150) # Fond pour le texte pour qu'il soit visible 

# Position de la boule
player_pos = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# Touche pour changer la couleur du fond
couleurs_fond_map = {
    'R (Noir)': (0, 0, 0),
    'F (Blanc)': (255, 255, 255),
    'C (Violet)': (128, 0, 128),
    'T (Jaune)': (255, 255, 0),
    'G (Cyan)': (0, 255, 255),
    'V (Orange)': (255, 165, 0),
}
couleurs_fond = list(couleurs_fond_map.values())
keys_fond = list(couleurs_fond_map.keys())

# Touche pour changer la couleur de la boule
couleurs_boule_map = {
    'Y (Rouge)': (255, 0, 0),
    'H (Vert)': (0, 255, 0),
    'B (Bleu)': (0, 0, 255),
    'U (Jaune)': (255, 255, 0),
    'J (Magenta)': (255, 0, 255),
    'N (Cyan)': (0, 255, 255),
}
couleurs_boule = list(couleurs_boule_map.values())
keys_boule = list(couleurs_boule_map.keys())


index_fond = 0
index_boule = 0

# Police d'écriture pour le texte à gauche de l'écran
FONT = pygame.font.SysFont("Arial", FONT_SIZE, bold=True)

def display_help(surface, x, y):
    
    help_lines = [ # Tableau pour donner à quoi servent les touches
        "COMMANDES :",
        "  Mouvement : Z, Q, S, D",
        "",
        "  Couleur Fond :",
        f"    R : {keys_fond[0]}",
        f"    F : {keys_fond[1]}",
        f"    C : {keys_fond[2]}",
        f"    T : {keys_fond[3]}",
        f"    G : {keys_fond[4]}",
        f"    V : {keys_fond[5]}",
        "",
        "  Couleur Boule :",
        f"    Y : {keys_boule[0]}",
        f"    H : {keys_boule[1]}",
        f"    B : {keys_boule[2]}",
        f"    U : {keys_boule[3]}",
        f"    J : {keys_boule[4]}",
        f"    N : {keys_boule[5]}",
    ]
    
    line_spacing = FONT_SIZE + 6 # Espacement entre les lignes pour que ce soit bien lisible
    padding_x = 5 # Marge horizontale pour le fond du texte
    padding_y = 2 # Marge verticale pour le fond du texte

    for i, line in enumerate(help_lines):
        # Pour ajouter le texte sur l'écran
        text_surface = FONT.render(line, True, TEXT_COLOR)

        # La taille est celle du texte plus le padding
        text_bg_surface = pygame.Surface((text_surface.get_width() + 2 * padding_x, text_surface.get_height() + 2 * padding_y), pygame.SRCALPHA)
        text_bg_surface.fill(BG_TEXT_COLOR) # Remplir avec la couleur du fond du tableau
        
        # Position où dessiner la ligne
        current_y = y + i * line_spacing
        
        # Ajouter le fond du texte
        surface.blit(text_bg_surface, (x, current_y))
        # Mettre le texte sur le fond 
        surface.blit(text_surface, (x + padding_x, current_y + padding_y))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.K_ESCAPE: # Ajouter une touche pour quitter facilement
            running = False
        if event.type == pygame.KEYDOWN:
            # Changer couleur du fond
            if event.key == pygame.K_r:
                index_fond = 0
            elif event.key == pygame.K_f:
                index_fond = 1
            elif event.key == pygame.K_c:
                index_fond = 2
            elif event.key == pygame.K_t:
                index_fond = 3
            elif event.key == pygame.K_g:
                index_fond = 4
            elif event.key == pygame.K_v:
                index_fond = 5

            # Changer couleur de la boule
            elif event.key == pygame.K_y:
                index_boule = 0
            elif event.key == pygame.K_h:
                index_boule = 1
            elif event.key == pygame.K_b:
                index_boule = 2
            elif event.key == pygame.K_u:
                index_boule = 3
            elif event.key == pygame.K_j:
                index_boule = 4
            elif event.key == pygame.K_n:
                index_boule = 5

    # Déplacement de la boule avec Z/Q/S/D
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_q]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # Fond
    screen.fill(couleurs_fond[index_fond])

    # Boule
    pygame.draw.circle(screen, couleurs_boule[index_boule], player_pos, RADIUS)
    
    # Afficher le tableau
    display_help(screen, 10, 10) 

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()

import pygame, sys
from button import Button

pygame.init()

# Create window
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def get_font(size):
    return pygame.font.Font("assets/arial_1.ttf", size)

# Main menu screen
def main_menu():
    pygame.display.set_caption("Colors Around the World")

    while True:
        SCREEN.fill("black")

        MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("assets/button.png"), pos=(640, 250), text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        # Button Handler
        for button in [PLAY_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)

        # Event handler
        for event in pygame.event.get():
            # Quit application
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MOUSE_POS):
                    print("PLAY!")

        # Update display
        pygame.display.update()

main_menu()

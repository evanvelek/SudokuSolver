import pygame

def run():
    pygame.init()

    surface = pygame.display.set_mode((400, 600), pygame.RESIZABLE)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == '__main__':
    run()
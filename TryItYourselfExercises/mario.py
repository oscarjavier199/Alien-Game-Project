import sys
import pygame

class EmptyScreen:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Empty Screen")
        self.bg_color = (142, 177, 145)

    def run_window(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            print()
            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    es = EmptyScreen()
    es.run_window()
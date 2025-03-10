from scripts.engine.engine_display import EngineDisplay
import pygame
import sys


# Engine class, core of the game.
class Engine:
    def __init__(self):
        pygame.init()
        self.display = EngineDisplay(self)

    # Run the game.
    def run(self):
        while True:
            # Temp code that should be inside each scene.
            # I suppose I could make an input singleton? But singletons are weird.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.display.update()

    # Static because it should be callable wherever?
    @staticmethod
    def quit():
        pass


# Create the engine and run it.
if __name__ == '__main__':
    Engine().run()
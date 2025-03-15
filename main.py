from scripts.engine.engine_scene_manager import EngineSceneManager
from scripts.engine.engine_display import EngineDisplay
import pygame
import sys


# Engine class, core of the game.
class Engine:

    #
    def __init__(self):
        pygame.init()
        self.display = EngineDisplay(self)
        self.scene_manager = EngineSceneManager(self)

    # Run the game.
    def run(self) -> None:
        while True:
            events = pygame.event.get()
            self.scene_manager.current_scene.update(events, self.display.display, False, self.display.delta_time)
            self.display.update()

    # Static because it should be callable wherever?
    @staticmethod
    def quit() -> None:
        pygame.quit()
        sys.exit()


# Create the engine and run it.
if __name__ == '__main__':
    Engine().run()
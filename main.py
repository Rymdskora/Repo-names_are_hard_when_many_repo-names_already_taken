from scripts.engine.engine_scene_manager import EngineSceneManager
from scripts.engine.engine_animator import EngineAnimator
from scripts.engine.engine_display import EngineDisplay
import pygame
import sys


# Engine class, core of the game.
class EmberEngine:

    #
    def __init__(self):
        pygame.init()
        self.display = EngineDisplay(self)
        self.animator = EngineAnimator(self)
        self.scene_manager = EngineSceneManager(self)

    # Run the game.
    def run(self) -> None:
        while True:
            events = pygame.event.get()
            self.animator.update()
            self.scene_manager.current_scene.update(
                events, self.display.display, self.animator.animate, self.display.delta_time)
            self.display.update()


    # Static because it should be callable wherever?
    @staticmethod
    def quit() -> None:
        pygame.quit()
        sys.exit()


# Create the engine and run it.
if __name__ == '__main__':
    EmberEngine().run()
from scripts.engine.engine_base import EngineBase
import pygame


# Display component of the engine.
class EngineDisplay(EngineBase):
    def __init__(self, engine):
        super().__init__(engine)
        # Make this dynamic and changeable, should have the option to change display resolution / flags.
        # I could always have an internal screen that is blitted to, then that is scaled to the display's
        # resolution and blitted to it?
        self.display = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
        self.timekeeper = pygame.time.Clock()
        self.framerate = 60
        self.delta_time = 0

    # Update the display, then repaint it once it has been updated.
    def update(self) -> None:
        # Divide by 1000 to change from milliseconds to seconds?
        self.delta_time = self.timekeeper.tick(self.framerate) / 1000
        pygame.display.flip()
        self.display.fill('black')
from scripts.engine.engine_base import EngineBase
import pygame


#
class EngineAnimator(EngineBase):

    #
    def __init__(self, game):
        super().__init__(game)
        self.animate = False
        self.animation_cooldown = 75
        self.last_animated = 0

    #
    def should_animate(self):
        current_time = pygame.time.get_ticks()
        if current_time >= self.animation_cooldown + self.last_animated:
            self.last_animated = current_time
            self.animate = True
        else:
            self.animate = False

    #
    def update(self):
        self.should_animate()
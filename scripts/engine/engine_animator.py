from scripts.engine.engine_base import EngineBase
import pygame


# The Engine Animator Class.
# Tracks and updates the state of whether sprites animate.
class EngineAnimator(EngineBase):

    # Self-explanatory.
    def __init__(self, game):
        super().__init__(game)
        self.animate = False
        self.animation_cooldown = 75
        self.last_animated = 0

    # Determines if sprites should animate based on time.
    def should_animate(self):
        current_time = pygame.time.get_ticks()
        if current_time >= self.animation_cooldown + self.last_animated:
            self.last_animated = current_time
            self.animate = True
        else:
            self.animate = False

    # Self-explanatory.
    def update(self):
        self.should_animate()
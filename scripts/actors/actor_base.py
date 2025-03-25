from typing import Tuple
import pygame


#
class ActorBase(pygame.sprite.Sprite):

    #
    def __init__(self, orchestrator, animator, physicist, position: Tuple[int, int], *groups):
        super().__init__(groups)
        self.orchestrator = orchestrator.set_entity(self)
        self.animator = animator.set_entity(self)
        self.physicist = physicist.set_entity(self)

        self.direction = pygame.Vector2(0, 0)
        self.image = self.animator.get_initial_frame()
        self.rect = self.image.get_frect(center=position)

    #
    def update(self, delta_time: float, animate: bool):
        self.animator.update(animate)
        self.physicist.update(delta_time)
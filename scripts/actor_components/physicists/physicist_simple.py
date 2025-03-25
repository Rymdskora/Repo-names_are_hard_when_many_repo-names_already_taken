from scripts.actor_components.physicists.physicist_interface import PhysicistInterface
from scripts.actor_components.component_base import ComponentBase
import pygame


#
class PhysicistSimple(ComponentBase, PhysicistInterface):

    #
    def __init__(self):
        super().__init__()
        self.speed = 190

    #
    def move(self, delta_time: float):
        if self.entity.direction.magnitude() != 0:
            movement = self.entity.direction.normalize() * self.speed * delta_time
            self.entity.rect.center += movement

    #
    def update(self, delta_time: float):
        self.move(delta_time)
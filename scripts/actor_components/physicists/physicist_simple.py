from scripts.actor_components.physicists.physicist_interface import PhysicistInterface
import pygame


#
class PhysicistSimple(PhysicistInterface):

    #
    def __init__(self):
        self.speed_states = {
            'idle': 0,
            'walk': 125,
            'run': 190,
            'crouch': 60,
        }
        self.speed = self.speed_states['idle']

    #
    def set_state(self, state: str):
        self.speed = self.speed_states[state]

    #
    def move(self, actor, delta_time: float):
        if actor.direction.magnitude() != 0:
            movement = actor.direction.normalize() * self.speed * delta_time
            actor.rect.center += movement

    #
    def update(self, actor, delta_time: float):
        self.move(actor, delta_time)
from typing import Tuple
import pygame


#
class ActorBase(pygame.sprite.Sprite):

    #
    def __init__(self, animator, physicist, position: Tuple[int, int], states, *groups):
        super().__init__(groups)
        self.animator = animator
        self.physicist = physicist

        self.image = self.animator.get_initial_frame()
        self.rect = self.image.get_frect(center=position)

        self.direction = pygame.Vector2(0, 0)
        self.states = states
        self.current_state = self.states[0]

    #
    def set_component_states(self, state: str) -> None:
        if state in self.states:
            if state != self.current_state:
                self.current_state = state
                self.animator.set_state(state)
                self.physicist.set_state(state)
            else:
                pass
        else:
            raise ValueError(f'State: {state} not in {self.states}!')

    #
    def update(self, delta_time: float, animate: bool):
        self.animator.update(self, animate)
        self.physicist.update(self, delta_time)
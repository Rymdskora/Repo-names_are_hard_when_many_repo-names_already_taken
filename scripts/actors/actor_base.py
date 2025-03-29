from data.definitions.flags import Flags
from typing import Tuple
import pygame


#
class ActorBase(pygame.sprite.Sprite):

    #
    def __init__(self, animator, physicist, sentinel, position: Tuple[int, int], states, *groups):
        super().__init__(groups)
        self.animator = animator
        self.physicist = physicist
        self.sentinel = sentinel

        self.image = self.animator.get_initial_frame()
        self.rect = self.image.get_frect(center=position)

        self.direction = pygame.Vector2(0, 0)
        self.states = states
        self.current_state = self.states[0]

        # Hold a certain state because of condition(s)?
        self.steady_state = False

    #
    def __repr__(self):
        pass

    #
    def set_component_state(self, component: str, state: str) -> None:
        state_contained = state in self.states
        component_contained = hasattr(self, component)

        if state_contained and component_contained:
            self.__dict__[component].set_state(state)
        elif not state_contained:
            raise ValueError(f'State: "{state}" is not in {self.states}!')
        elif not component_contained:
            raise AttributeError(f'Component: "{component}" is not in {self.__dict__}!')

    #
    def set_component_states(self, state: str) -> None:
        if state in self.states:
            if state != self.current_state:
                self.current_state = state
                self.animator.set_state(state)
                self.physicist.set_state(state)
                self.sentinel.set_state(state)
            else:
                pass
        else:
            raise ValueError(f'State: "{state}" not in {self.states}!')

    #
    def manage_flags(self, flags: Flags) -> None:
        if flags != 0:
            if flags & Flags.EXHAUSTED:
                pass

    #
    def update(self, delta_time: float, animate: bool):
        self.animator.update(self, animate)
        self.physicist.update(self, delta_time)
        flags = self.sentinel.update(self)
        self.manage_flags(flags)
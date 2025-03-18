from scripts.actor_components.animators.animator_interface import AnimatorInterface
from scripts.actor_components.component_base import ComponentBase
from typing import Dict, List
import pygame


# TODO - Eventually, I need to create a way to blend between frames when state changes.
class AnimatorDict(ComponentBase, AnimatorInterface):

    #
    def __init__(self, sprites: Dict[str, List[pygame.Surface]], state='idle'):
        super().__init__()
        self.sprite_dictionary = sprites
        self.state = state
        self.num_sprites = len(self.sprite_dictionary[self.state])
        self.current_frame = 0
        self.state_changed = False

    #
    def set_animation_state(self, state: str):
        # If running in a specific direction, run needs to be flipped based on
        # the direction the character is moving horizontally.
        # I'm sure others will need to be flipped too.

        valid_states = ['idle', 'run', 'crouch', 'jump', 'fall']
        if state in valid_states:
            self.state = state
            self.current_frame = 0
            # Change the number of sprites in the list when the state changes
            # because the lists MAY have different lengths (hopefully not, w/e).
            self.num_sprites = len(self.sprite_dictionary[self.state])
            self.state_changed = True
        else:
            raise ValueError(f'State {state} is not a valid state!')

    #
    def get_initial_frame(self) -> pygame.Surface:
        return self.sprite_dictionary[self.state][self.current_frame]

    #
    def on_animate(self) -> None:
        if self.state_changed is False:
            self.current_frame += 1
            # Overstepped index, loop back to start of the animation.
            if self.current_frame >= self.num_sprites:
                self.current_frame = 0
        self.entity.image = self.sprite_dictionary[self.state][self.current_frame]
        self.state_changed = False

    #
    def update(self, animate: bool) -> None:
        if animate is True:
            self.on_animate()
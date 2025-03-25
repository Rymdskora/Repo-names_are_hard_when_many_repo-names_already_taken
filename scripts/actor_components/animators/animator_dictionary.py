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
        self.current_state = state
        self.current_frame = 0
        self.facing = 'right'
        self.num_sprites = len(self.sprite_dictionary[self.current_state])

    #
    def set_state(self, state: str) -> None:
        self.current_state = state
        self.current_frame = 0
        self.num_sprites = len(self.sprite_dictionary[self.current_state])
            
    #
    def get_initial_frame(self) -> pygame.Surface:
        return self.sprite_dictionary[self.current_state][self.current_frame]

    #
    def on_animate(self) -> None:
        self.current_frame += 1
        # Overstepped index, loop back to start of the animation.
        if self.current_frame >= self.num_sprites:
            self.current_frame = 0

        self.should_reflect()

        if self.facing == 'right':
            self.entity.image = self.sprite_dictionary[self.current_state][self.current_frame]
        else:
            self.entity.image = self.get_reflected_frame()

    #
    def should_reflect(self):
        if self.entity.direction.x == 1:
            self.facing = 'right'
        elif self.entity.direction.x == -1:
            self.facing = 'left'

    # Only flips across the horizontal surface as I don't think I'll ever need a vertical flip!
    def get_reflected_frame(self) -> pygame.Surface:
        frame = self.sprite_dictionary[self.current_state][self.current_frame]
        flipped_frame = pygame.transform.flip(frame, True, False)
        return flipped_frame

    #
    def update(self, animate: bool) -> None:
        if animate is True:
            self.on_animate()
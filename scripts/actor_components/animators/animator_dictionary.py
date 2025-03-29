from scripts.actor_components.animators.animator_interface import AnimatorInterface
from typing import Dict, List
import pygame


# TODO - Eventually, I need to create a way to blend between frames when state changes.
class AnimatorDict(AnimatorInterface):

    #
    def __init__(self, sprites: Dict[str, List[pygame.Surface]], state='idle'):
        self.sprite_dictionary = sprites
        self.state = state
        self.current_frame = 0
        self.facing = 'right'
        self.num_sprites = len(self.sprite_dictionary[self.state])

    #
    def set_state(self, state: str) -> None:
        self.state = state
        self.current_frame = 0
        self.num_sprites = len(self.sprite_dictionary[self.state])
            
    #
    def get_initial_frame(self) -> pygame.Surface:
        return self.sprite_dictionary[self.state][self.current_frame]

    #
    def on_animate(self, actor) -> None:
        self.current_frame += 1
        # Overstepped index, loop back to start of the animation.
        if self.current_frame >= self.num_sprites:
            self.current_frame = 0

        self.should_reflect(actor)

        if self.facing == 'right':
            actor.image = self.sprite_dictionary[self.state][self.current_frame]
        else:
            actor.image = self.get_reflected_frame()

    #
    def should_reflect(self, actor):
        if actor.direction.x == 1:
            self.facing = 'right'
        elif actor.direction.x == -1:
            self.facing = 'left'

    # Only flips across the horizontal surface as I don't think I'll ever need a vertical flip!
    def get_reflected_frame(self) -> pygame.Surface:
        frame = self.sprite_dictionary[self.state][self.current_frame]
        flipped_frame = pygame.transform.flip(frame, True, False)
        return flipped_frame

    #
    def update(self, actor, animate: bool) -> None:
        if animate is True:
            self.on_animate(actor)
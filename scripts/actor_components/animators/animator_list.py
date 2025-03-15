from scripts.actor_components.animators.animator_interface import AnimatorInterface
from scripts.actor_components.component_base import ComponentBase
from typing import List
import pygame


# List-based Animator component.
class AnimatorList(ComponentBase, AnimatorInterface):

    #
    def __init__(self, sprites: List[pygame.Surface]):
        super().__init__()
        self.sprite_list = sprites
        self.num_sprites = len(self.sprite_list)
        self.current_frame = 0

    # pygame.sprite.Sprite needs the actor to have an image,
    # so we return the first image in our list to the actor.
    def get_initial_frame(self) -> pygame.Surface:
        return self.sprite_list[self.current_frame]

    #
    def on_animate(self) -> None:
        self.current_frame += 1
        # Oh shit, we've overstepped our index, loop back to the first frame!
        # If this was C we'd just run into some random block of memory like real programmers do.
        if self.current_frame >= self.num_sprites:
            self.current_frame = 0
        self.entity.image = self.sprite_list[self.current_frame]

    #
    def update(self, animate: bool) -> None:
        if animate is True:
            self.on_animate()
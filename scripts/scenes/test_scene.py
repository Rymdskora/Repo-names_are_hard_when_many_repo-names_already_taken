from scripts.actor_components.animators.animator_list import AnimatorList
from scripts.actors.actor_base import ActorBase

from scripts.scenes.scene_base import SceneBase
import pygame


# Test scene.
class SceneTestScene(SceneBase):

    #
    def __init__(self, engine):
        super().__init__(engine)

    #
    def update(self, events, screen: pygame.Surface, animate: bool, delta_time) -> None:
        for event in events:
            if event.type == pygame.QUIT:
                self.engine.quit()

        self.draw(screen)

    #
    def draw(self, screen: pygame.Surface) -> None:
        pass
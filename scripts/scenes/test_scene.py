from scripts.factories.factory_actor import FactoryActor
from scripts.scenes.scene_base import SceneBase
import pygame


# Test scene.
class SceneTestScene(SceneBase):

    # Self-explanatory.
    def __init__(self, engine):
        super().__init__(engine)

        self.flip = False
        self.animate = False
        self.animate_cooldown = 75
        self.last_animated = 0
        self.sprites = pygame.sprite.Group()
        self.dict_actor = FactoryActor.create_actor((256, 256), self.sprites, returned=True)

    # Self-explanatory.
    def update(self, events, screen: pygame.Surface, animate: bool, delta_time: float) -> None:
        for event in events:
            if event.type == pygame.QUIT:
                self.engine.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.flip = not self.flip
                if self.flip is True:
                    state = 'run'
                else:
                    state = 'idle'
                self.dict_actor.animator.set_animation_state(state)

        self.sprites.update(delta_time, animate)
        self.draw(screen)

    # Self-explanatory.
    def draw(self, screen: pygame.Surface) -> None:
        self.sprites.draw(screen)

from scripts.controllers.commands.command_move import CommandMove

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

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_d]:
            if keys_pressed[pygame.K_LSHIFT]:
                self.dict_actor.orchestrator.set_states('run')
            elif keys_pressed[pygame.K_LCTRL]:
                self.dict_actor.orchestrator.set_states('crouch')
            else:
                self.dict_actor.orchestrator.set_states('walk')
            CommandMove.execute('right', self.dict_actor)
        elif keys_pressed[pygame.K_a]:
            if keys_pressed[pygame.K_LSHIFT]:
                self.dict_actor.orchestrator.set_states('run')
            elif keys_pressed[pygame.K_LCTRL]:
                self.dict_actor.orchestrator.set_states('crouch')
            else:
                self.dict_actor.orchestrator.set_states('walk')
            CommandMove.execute('left', self.dict_actor)
        else:
            CommandMove.execute('none', self.dict_actor)
            self.dict_actor.orchestrator.set_states('idle')

        self.sprites.update(delta_time, animate)
        self.draw(screen)

    # Self-explanatory.
    def draw(self, screen: pygame.Surface) -> None:
        self.sprites.draw(screen)

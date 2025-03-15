import pygame


#
class ActorBase(pygame.sprite.Sprite):

    #
    def __init__(self, animator, groups):
        super().__init__(*groups)
        self.animator = animator.set_entity(self)

        self.image = self.animator.get_initial_frame()
        self.rect = self.image.get_rect()

    #
    def update(self, delta_time, animate: bool):
        self.animator.update(animate)
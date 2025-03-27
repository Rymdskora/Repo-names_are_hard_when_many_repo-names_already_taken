from abc import ABC, abstractmethod
import pygame


#
class AnimatorInterface(ABC):

    #
    @abstractmethod
    def get_initial_frame(self) -> pygame.Surface:
        pass

    #
    @abstractmethod
    def get_reflected_frame(self) -> pygame.Surface:
        pass

    #
    @abstractmethod
    def on_animate(self, actor) -> None:
        pass

    #
    @abstractmethod
    def update(self, actor, animate: bool) -> None:
        pass
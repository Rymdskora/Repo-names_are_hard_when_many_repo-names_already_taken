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
    def get_flipped_frame(self) -> pygame.Surface:
        pass

    #
    @abstractmethod
    def on_animate(self) -> None:
        pass

    #
    @abstractmethod
    def update(self, animate: bool) -> None:
        pass
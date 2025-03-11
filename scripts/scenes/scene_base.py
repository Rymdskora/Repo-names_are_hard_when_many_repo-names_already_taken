from abc import ABC, abstractmethod
import pygame


# Scene interface I'll use to define concrete scenes.
class SceneBase(ABC):
    def __init__(self, engine):
        self.engine = engine

    #
    @abstractmethod
    def update(self, events, screen: pygame.Surface, animate: bool, delta_time) -> None:
        pass

    #
    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        pass
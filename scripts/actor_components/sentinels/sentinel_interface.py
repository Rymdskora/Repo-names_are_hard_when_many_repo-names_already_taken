from abc import ABC, abstractmethod


#
class SentinelInterface(ABC):

    #
    @abstractmethod
    def set_state(self, state: str) -> None:
        pass

    #
    @abstractmethod
    def update(self, actor) -> int:
        pass
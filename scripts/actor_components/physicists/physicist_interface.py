from abc import ABC, abstractmethod


#
class PhysicistInterface(ABC):

    #
    @abstractmethod
    def move(self, delta_time: float):
        pass

    #
    @abstractmethod
    def update(self, delta_time: float):
        pass
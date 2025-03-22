from abc import ABC, abstractmethod


#
class CommandBase(ABC):

    #
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass
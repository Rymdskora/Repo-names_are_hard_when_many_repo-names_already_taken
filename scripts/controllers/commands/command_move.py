from scripts.controllers.commands.command_base import CommandBase


#
class CommandMove(CommandBase):
    
    #
    @staticmethod
    def execute(direction: str, actor):
        if direction == "left":
            actor.direction.x = -1
        elif direction == "right":
            actor.direction.x = 1
        else:
            actor.direction.x = 0
from scripts.actor_components.physicists.physicist_simple import PhysicistSimple
from scripts.actor_components.animators.animator_dictionary import AnimatorDict
from scripts.actor_components.animators.animator_list import AnimatorList
from scripts.actors.actor_base import ActorBase
from scripts.helpers.helper_sprite_loader import HelperSpriteLoader
from typing import Tuple


#
class FactoryActor:

    #
    @classmethod
    def create_actor(cls, position: Tuple[int, int], groups, returned=False):
        idle = HelperSpriteLoader.load_sprite('_Idle.png', (120, 80), 2)
        run = HelperSpriteLoader.load_sprite('_Run.png', (120, 80), 2)
        sprite_states = {
            'idle': idle,
            'run': run,
        }

        animator_dict = AnimatorDict(sprite_states)
        physicist = PhysicistSimple()

        actor = ActorBase(animator_dict, physicist, position, groups)

        if returned is not False:
            return actor
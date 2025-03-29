from scripts.actor_components.sentinels.sentinel_simple import SentinelSimple
from scripts.actor_components.physicists.physicist_simple import PhysicistSimple
from scripts.actor_components.animators.animator_dictionary import AnimatorDict
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
        crouch = HelperSpriteLoader.load_sprite('_CrouchWalk.png', (120, 80), 2)
        sprite_states = {
            'idle': idle,
            'walk': run,
            'run': run,
            'crouch': crouch,
        }


        available_states = ['idle', 'walk', 'run', 'crouch']

        animator_dict = AnimatorDict(sprite_states)
        physicist = PhysicistSimple()
        sentinel = SentinelSimple()

        actor = ActorBase(animator_dict, physicist, sentinel, position, available_states, groups)

        if returned is not False:
            return actor
from scripts.actor_components.sentinels.sentinel_interface import SentinelInterface
from data.definitions.flags import Flags
import pygame


#
class SentinelSimple(SentinelInterface):

    # TODO - Load these from JSON files (On a per-Actor basis?).
    def __init__(self, state='idle'):
        self.flags = 0
        self.state = state
        self.statuses = {  # Examples for later?!
            'slowed': [False, 0],
            'burning': [False, 0],
            # etc.
        }
        self.health = {
            'min': 0,
            'max': 100,
            'current': 100,
            'regeneration': 1,
            'regeneration_delay': 1000,  # Milliseconds!
            'last_regenerated': 0,
        }
        self.mana = {
            'min': 0,
            'max': 100,
            'current': 100,
            'regeneration': 1,
            'regeneration_delay': 1000,  # Milliseconds!
            'last_regenerated': 0,
        }
        self.stamina = {
            'min': 0,
            'max': 100,
            'current': 100,
            'consumption': 10,
            'regeneration': 10,
            'regeneration_delay': 1000,  # Milliseconds!
            'last_regenerated': 0,
        }

    #
    def set_state(self, state: str) -> None:
        self.state = state

    #
    def manage_flags(self):
        if self.flags & Flags.EXHAUSTED:
            if self.stamina['current'] >= self.stamina['max'] * 0.25:
                Flags.lower_component_flag(self, Flags.EXHAUSTED)

    #
    def manage_stamina(self, current_time: int):
        if current_time >= self.stamina['regeneration_delay'] + self.stamina['last_regenerated']:
            self.stamina['last_regenerated'] = current_time
            should_tick = True
        else:
            should_tick = False

        if not self.flags & Flags.EXHAUSTED and self.state == 'run':
            post_run_stamina = self.stamina['current'] - self.stamina['consumption']
            if post_run_stamina >= 0 and should_tick:
                self.stamina['current'] = post_run_stamina
                if post_run_stamina <= 0:
                    Flags.raise_component_flag(self, Flags.EXHAUSTED)
        else:
            if (self.stamina['current'] < self.stamina['max']) and should_tick:
                self.stamina['current'] += self.stamina['regeneration']

    #
    def update(self, actor) -> int:
        # Eventually, just call time once and pass it around in the main loop?!
        current_time = pygame.time.get_ticks()
        self.manage_stamina(current_time)
        self.manage_flags()
        return self.flags
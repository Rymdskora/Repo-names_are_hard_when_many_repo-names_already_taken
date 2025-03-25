from scripts.actor_components.component_base import ComponentBase


#
class OrchestratorActor(ComponentBase):

    #
    def __init__(self):
        super().__init__()
        self.states = ['idle', 'walk', 'run', 'crouch', 'jump', 'fall']
        self.current_state = self.states[0]
        self.last_state = self.current_state

    #
    def set_state(self, state: str) -> None:
        if state in self.states:
            if state != self.current_state:
                self.current_state = state
                self.entity.animator.set_state(state)
            else:
                pass
        else:
            raise ValueError(f'State: {state} not in {self.states}!')

    #
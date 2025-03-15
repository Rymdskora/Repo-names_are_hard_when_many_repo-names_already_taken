# Base Component for all other components.
# Components need to know about the object their composed with.
class ComponentBase:

    # Need to tell the component we're going to have an entity here.
    def __init__(self):
        self.entity = None

    # Allows the component to return itself to the entity inside
    # the entity's constructor.
    def set_entity(self, entity):
        self.entity = entity
        return self

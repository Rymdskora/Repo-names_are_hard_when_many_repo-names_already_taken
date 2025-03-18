# Engine component base class, should be inherited by all the engine components.
# It's just an easy way to not have to have the same code smeared across a bunch of classes.
class EngineBase:

    # Self-explanatory.
    def __init__(self, engine):
        self.engine = engine
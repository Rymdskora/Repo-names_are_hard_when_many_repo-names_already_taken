#
class Flags:

    # Bitwise shenanigans for throwing up
    # multiple status flags at a later date!
    EXHAUSTED = 1 << 0

    #
    @classmethod
    def check_flag_existence(cls, flag) -> None:
        known_flags = [cls.EXHAUSTED]
        if flag not in known_flags:
            raise Exception(f'Flag {flag} does not exist!')

    # No need to check flag existence here because
    # they're already checked when a component raises them!
    @classmethod
    def manage_actor_flags(cls, actor, flags) -> None:
        added_flags = flags & ~actor.flags  # New flags that aren't already set
        removed_flags = actor.flags & ~flags  # Old flags that are no longer present

        actor.flags |= added_flags  # Add new flags
        actor.flags &= ~removed_flags  # Remove flags that are no longer active

    #
    @classmethod
    def raise_component_flag(cls, component, flag) -> None:
        cls.check_flag_existence(flag)
        component.flags |= flag

    #
    @classmethod
    def lower_component_flag(cls, component, flag) -> None:
        cls.check_flag_existence(flag)
        component.flags &= ~flag
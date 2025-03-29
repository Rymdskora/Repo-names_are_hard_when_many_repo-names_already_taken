#
class Flags:

    # Bitwise shenanigans for throwing up
    # multiple status flags at a later date!
    EXHAUSTED = 1 << 0

    #
    @classmethod
    def check_flag_existence(cls, flag):
        known_flags = [cls.EXHAUSTED]
        if flag not in known_flags:
            raise Exception(f'Flag {flag} does not exist!')

    #
    @classmethod
    def raise_component_flag(cls, component, flag):
        cls.check_flag_existence(flag)
        component.flags |= flag

    #
    @classmethod
    def lower_component_flag(cls, component, flag):
        cls.check_flag_existence(flag)
        component.flags &= ~flag
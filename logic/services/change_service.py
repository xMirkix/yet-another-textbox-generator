class Changes:
    _changed = False

    @classmethod
    def saved(cls):
        cls._changed = False

    @classmethod
    def change(cls):
        cls._changed = True

    @classmethod
    def get_state(cls) -> bool:
        return cls._changed
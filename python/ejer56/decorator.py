class Decorator:
    def __init__(self, decorate):
        self._decorate = decorate

    def __getattr__(self, attr):
        return getattr(self._decorate, attr)

    def __setattr__(self, attr, attr_value):
        if not attr.startswith('_'):
            setattr(self._decorate, attr, attr_value)
        else:
            super().__setattr__(attr, attr_value)

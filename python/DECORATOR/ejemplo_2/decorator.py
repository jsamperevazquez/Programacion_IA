

class Decorator:
    def __init__(self, decorado):
        self._decorado = decorado

    def __getattr__(self, attr):
        print('__getattr__ ', attr)
        return getattr(self._decorado, attr)

    def __setattr__(self, attr, attr_value):
        print('__setattr__ ', attr)
        if not attr.startswith('_'):
            setattr(self._decorado, attr, attr_value)
        else:
            super().__setattr__(attr, attr_value)

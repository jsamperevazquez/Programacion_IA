from component import Text


class TextDecorator(Text):
    def __init__(self, text_component):
        self._text_component = text_component

    def render(self):
        return self._text_component.render()

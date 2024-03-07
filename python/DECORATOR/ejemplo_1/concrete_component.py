from component import Text


class PlainText(Text):
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text

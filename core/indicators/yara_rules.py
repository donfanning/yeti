import yara

from core.indicators import Indicator


class Yara(Indicator):

    def __init__(self, *args, **kwargs):
        super(Yara, self).__init__(*args, **kwargs)
        if self.pattern:
            self.compiled_yara = yara.compile(source=self.pattern)

    def match(self, value):
        matches = self.compiled_yara.match(data=value)
        return True if matches else False

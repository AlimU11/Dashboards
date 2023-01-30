from .StrEnum import StrEnum


class Colors(StrEnum):
    def opacity(self, opacity: float) -> str:
        return self.value.replace('(', 'a(').replace(')', f', {opacity})')

    @staticmethod
    def colorpalette() -> list[str]:
        return [Colors.blue, Colors.green, Colors.purple, Colors.red]

    black = 'rgb(42, 63, 95)'
    white = 'rgb(255, 255, 255)'
    grey = 'rgb(153, 153, 153)'
    green = 'rgb(0, 204, 150)'
    blue = 'rgb(99, 110, 250)'
    pink = 'rgb(255, 102, 146)'
    yellow = 'rgb(254, 203, 82)'
    red = 'rgb(220, 57, 18)'
    purple = 'rgb(171, 99, 250)'
    orange = 'rgb(255, 127, 14)'

    transparent = 'rgba(0, 0, 0, 0)'

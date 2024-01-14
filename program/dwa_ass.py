"""
    Основной файл программы помощника Dopewars
"""

from dataclasses import dataclass
from dwa_consts import ALL_DRAGS, ALL_LOCATIONS, GUNS, WINDOW_SIZE


@dataclass
class Player:
    """Описание данных игрока"""

    drugs: dict  # наименование и количество товара в наличии
    guns: dict  # наименование и количество оружия
    place: str  # текущее местонахождение
    cash: int  # количество наличных денег при себе
    deposit: int  # количество денег на депозите в банке
    space: int  # полное количество слотов

    def __init__(self):
        self.drugs = {}
        for item in ALL_DRAGS:
            drug = {"quantity": 0, "price": 0}
            self.drugs.update({item: drug})
        self.place = ALL_LOCATIONS[0]
        self.cash = 2000
        self.deposit = 0
        self.space = 100
        self.guns = {}
        for gun in GUNS:
            self.guns.update({gun: 0})


if __name__ == "__main__":
    player = Player()
    dw_gui()

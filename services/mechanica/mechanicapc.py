import random
from services.mechanica.basemechanica import BaseMechanica


class MechanicaPC(BaseMechanica):

    def player2_input(self):
        return random.randint(0, len(self.player2.card_list) - 1)

from Model.CardMaker.CardFactory import CardFactory
from Model.dev_cards import Devcard


class DevCardFactory(CardFactory):
    def create_card(self, data_tuple):
        _, nine_message, nine_effect, ten_message, ten_effect, eleven_message, eleven_effect, item = data_tuple
        dev_card = Devcard(nine_message, nine_effect, ten_message, ten_effect,
                           eleven_message, eleven_effect, item)
        return dev_card

from Model.CardMaker.CardFactory import CardFactory
from Model.item import Item


class ItemFactory(CardFactory):
    def create_card(self, tuple_data):
        _, name, effect, can_combine, combines_with_1, combines_with_2, makes_1, makes_2, uses = tuple_data
        new_item = Item(name, effect, can_combine, [combines_with_1, combines_with_2], [makes_1, makes_2], uses)
        new_item.effect = getattr(new_item, effect, None)
        return new_item

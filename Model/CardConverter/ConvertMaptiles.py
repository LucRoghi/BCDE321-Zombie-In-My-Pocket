from Model.CardConverter.AbstractConvert import *
from Model.CardMaker.MaptileFactory import MaptileFactory
from Model.map_tile import MapTile


class ConvertMaptiles(AbstractConvert):
    def tuple_to_objects(self, tuple_list: [tuple]):
        tile_list = []
        maptile_factory = MaptileFactory()
        for tile in tuple_list:
            tile_list.append(maptile_factory.create_card(tile))
        return tile_list

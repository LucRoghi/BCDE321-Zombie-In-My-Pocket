import Model


class IndoorFactory(Model.AbstractFactory):
    def create_tile(self, name, effect=None, doors=None, x=16, y=16,
                    entrance=None):
        return Model.IndoorTile(name, effect, doors, x, y, entrance)
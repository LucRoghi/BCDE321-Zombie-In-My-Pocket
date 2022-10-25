import abfac


class IndoorFactory(abfac.AbstractFactory):
    def create_tile(self, name, effect=None, doors=None, x=16, y=16,
                    entrance=None):
        return abfac.IndoorTile(name, effect, doors, x, y, entrance)

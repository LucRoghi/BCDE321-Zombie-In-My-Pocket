import abfac


class OutdoorFactory(abfac.AbstractFactory):
    def create_tile(self, name, effect=None, doors=None, x=16, y=16,
                    entrance=None):
        return abfac.OutdoorTile(name, effect, doors, x, y, entrance)

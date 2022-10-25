from os import path


def read_file():
    _path = path.dirname(__file__)
    _path = path.join(_path, r'assets\DevCards.csv')

    with open(_path, 'r') as f:
        lines = f.readlines()

    return "".join(lines)


if __name__ == '__main__':
    print(read_file())

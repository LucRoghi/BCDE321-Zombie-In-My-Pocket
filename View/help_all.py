import json
import pandas as pd


def load_help():
    with open("help.json") as f:
        data = json.load(f)

    for i in data["Help Commands"]:
        print(i['cmd'])

import config
from itertools import groupby


def rel_x(percent):
    return float(config.screen_w) / 100 * percent


def rel_y(percent):
    return float(config.screen_h) / 100 * percent


def group_ingredients(ingredients):
    result = sorted(ingredients, key=lambda a: (a[0], a[1]))
    return [list(b) for a, b in groupby(result, lambda a: (a[0], a[1]))]
    

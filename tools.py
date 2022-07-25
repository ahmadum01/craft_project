import config

def rel_x(percent):
    return float(config.screen_w) / 100 * percent


def rel_y(percent):
    return float(config.screen_h) / 100 * percent

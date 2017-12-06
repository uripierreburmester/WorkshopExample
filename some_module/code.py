import numpy as np


def integrate_trapz(xs, ys):
    """ Document me"""
    widths = np.diff(xs)
    midpoints = 0.5 * (ys[1:] + ys[:-1])
    area = np.sum(widths * midpoints)
    return area

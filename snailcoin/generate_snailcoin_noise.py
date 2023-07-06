import random
import math

def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)

def lerp(a, b, t):
    return a + t * (b - a)

def grad(hash, x, y, z):
    h = hash & 15
    u = x if h < 8 else y
    v = y if h < 4 else (x if h == 12 or h == 14 else z)
    return (u if (h & 1) == 0 else -u) + (v if (h & 2) == 0 else -v)

def generate_snailcoin_noise(width, height, scale):
    grid = [[0 for _ in range(width)] for _ in range(height)]
    permutation = list(range(256))
    random.shuffle(permutation)
    permutation *= 2

    for y in range(height):
        for x in range(width):
            xf = x / scale
            yf = y / scale

            x0 = int(math.floor(xf))
            y0 = int(math.floor(yf))
            x1 = x0 + 1
            y1 = y0 + 1

            u = fade(xf - x0)
            v = fade(yf - y0)

            n00 = grad(permutation[permutation[x0] + y0], xf, yf, 0)
            n01 = grad(permutation[permutation[x0] + y1], xf, yf - 1, 0)
            n10 = grad(permutation[permutation[x1] + y0], xf - 1, yf, 0)
            n11 = grad(permutation[permutation[x1] + y1], xf - 1, yf - 1, 0)

            value = lerp(lerp(n00, n10, u), lerp(n01, n11, u), v)
            grid[y][x] = 1 if value > 0 else 0

    return grid

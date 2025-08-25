from itertools import cycle

colors = ['red', 'green', 'blue']

cycled_colors = cycle(colors)

for _ in range(6):
    print(next(cycled_colors))

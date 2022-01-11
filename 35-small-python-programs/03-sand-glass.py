def glass(rows):
    spaces = 0
    stars2 = 3
    spaces2 = rows - 2
    stars = 2 * rows - 1
    for i in range(1, rows + 1):
        print(" " * spaces + "*" * stars)
        stars -= 2
        spaces += 1
    for i in range(1, rows):
        print(" " * spaces2 + "*" * stars2)
        stars2 += 2
        spaces2 -= 1


glass(10)

def calculate_area(figure, *args):
    if figure == "rectangle":
        return args[0] * args[1]
    elif figure == "circle":
        return 3.14 * args[0] ** 2
    elif figure == "triangle":
        return (args[0] * args[1]) / 2
    else:
        return "Available figures are rectangle, circle and triangle"


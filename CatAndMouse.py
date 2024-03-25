def catAndMouse(x, y, z):
    catA = abs(z - x)
    catB = abs(z - y)

    if catA < catB:
        return "Cat A"
    elif catB < catA:
        return "Cat B"
    else:
        return "Mouse C"

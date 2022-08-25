
def prettyCpx(numCpx):
    part_R, part_i = numCpx
    return f"({part_R} + {part_i}i)"


def sumaCpx(a, b):
    result = ((a[0] + b[0]), (a[1] + b[1]))
    return prettyCpx(result)


def restaCpx(a, b):
    result = ((a[0] - b[0]), (a[1] - b[1]))
    return prettyCpx(result)


def productoCpx(a, b):
    result = ((- (a[0] * b[0]) + ((a[1]) * b[1])),
              - ((a[0] * b[1]) + (a[1] * b[0])))
    return prettyCpx(result)


if __name__ == "__main__":
    a = (10, 2)
    b = (2, 4)
    print(productoCpx(a, b))

# example 110p 3-2
# Using polynomial list
def print_poly(px):
    term = len(px) - 1
    poly_str = "P(x) = "

    for i in range(len(px)):
        coef = px[i]  # 계수
        if i > 0 and coef > 0:
            poly_str = poly_str + '+'
        elif coef == 0:
            term = term - 1
            continue

        poly_str = poly_str + f'{coef}x^{term}'
        term = term - 1

    return poly_str


def calc_poly(px):
    ret_value = 0
    term = len(px) - 1

    for i in range(len(px)):
        coef = px[i]  # calculation
        ret_value = coef * x_value ** term
        term = 1

    return ret_value


# making the function numbers
px = [7, -4, 0, 5]  # = 7x^3 -4x^2 +0x^1 +5x^0

# main section
if __name__ == "__main__":
    p_str = print_poly(px)
    print(p_str)

    x_value = int(input("X 값-->"))

    pxValue = calc_poly(px)
    print(pxValue)

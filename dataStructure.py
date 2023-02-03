# example 110p 3-2
# Using polynomial list
def printPoly(tx, px):
    polyStr = "P(x) = "

    for i in range(len(px)):
        term = tx[i]  # numbers
        coef = px[i]  # calculation

        if (coef >= 0):
            polyStr += "+"
        polyStr += str(coef) + "x^" + str(term) + " "

    return polyStr


def calcPoly(xVal, t_x, p_x):
    ret_value = 0

    for i in range(len(px)):
        term = t_x[i]  # 항 차수
        coef = p_x[i]  # 계수
        ret_value += coef * xValue ** term

    return ret_value


## 전역 변수 선언 부분 ##
tx = [300, 20, 0]
px = [3, -4, 5]

## 메인 코드 부분 ##
if __name__ == "__main__":
    pStr = printPoly(tx, px)
    print(pStr)

    xValue = int(input("X 값-->"))

    pxValue = calcPoly(xValue, tx, px)
    print(pxValue)

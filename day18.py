# Chapter 10
# recursion 10.2 ex
def openBox():
    global count
    print("Opening the box \(.˃ ᵕ ˂ )/ ")
    count -= 1
    if count == 0:
        print("Putting the ring inside ฅ^•ﻌ•^ฅ")
        return
    openBox()
    print("Closing the box ૮ ˙Ⱉ˙ ა")


count = 10
openBox()  # 처음 함수를 다시 호출

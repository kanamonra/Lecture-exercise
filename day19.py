# тусд нь үүсгээд хийж буй calculator

import tkinter as tk

memos = [None for _ in range(100)]  # 전역 리스트
memos[0], memos[1] = 0, 1


def fibo_memo_recu(n):
    """
    재귀함수에 Memoization(DP)을 사용한 피보나치 수열 처리 함수
    :param n:
    :return:
    """

    if n <= 1:
        return memos[n]

    if memos[n] is not None:  # 전역 메모리 memos에 이전에 계산한 결과 값이 존재하면
        return memos[n]

    memos[n] = fibo_memo_recu(n - 2) + fibo_memo_recu(n - 1)  # 처음 방문하는 n이면
    return memos[n]


def fact_recu(n):
    if n == 1:
        return 1
    else:
        return n * fact_recu(n - 1)

def fac_input():
    lbl_result.config(text=f'Result of fibonacci: {fact_recu(int(en_num_input.get()))}')




def fib_input():
    lbl_result.config(text=f'Result of fibonacci: {fibo_memo_recu(int(en_num_input.get()))}')



win = tk.Tk()
win.title('Calculator')

win.geometry("180x240")
en_num_input = tk.Entry()  # text enter
lbl_result = tk.Label(text='Result: ')
btn_fact = tk.Button(text="Factorial ", command=fac_input)
btn_fibo = tk.Button(text="Fibonacci ", command=fib_input)

en_num_input.pack()
lbl_result.pack()
btn_fact.pack(fill='x')
btn_fibo.pack(fill='x')

win.mainloop()

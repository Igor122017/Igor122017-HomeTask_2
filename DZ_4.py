# 4 Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов
# на указанных позициях. Позиции хранятся в списке positions - создайте этот список (например:
# positions = [1, 3, 6]).

numb = int(input("Введите  число N:  "))

pozit1 = int(input("Введите  индекс 1 числа : "))
pozit2 = int(input("Введите  индекс  2 числа : "))
pozit3 = int(input("Введите  индекс  3 числа : "))


def result_poziton (num, pz1, pz2, pz3):
    spisok = []
    pozit = [pz1, pz2, pz3]
    result = 1
    for i in range(-num, num+1):
        spisok.append(i)
    for j in pozit:
        result *= spisok[j]
    return print(f' произведение значений с введенным индексами  составляет {result}')


result_poziton(numb, pozit1, pozit2, pozit3)
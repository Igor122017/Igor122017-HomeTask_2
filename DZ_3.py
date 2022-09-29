# 3 Задать список из n чисел последовательности (1+ 1/n)^n и вывести на экран их сумму

number = int(input("Введите  число n: "))

def list_numbers(num):
    list = []
    for i in range(1, num+1):
        x = (1 + 1/i)**i
        list.append(x)
    return list

print(sum(list_numbers(number)))
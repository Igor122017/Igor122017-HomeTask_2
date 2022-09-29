# 1 Подсчитать сумму цифр в вещественном числе.

number = input("Введите вещественное число: ")
number = number.replace('.', '') 
number = number.replace(',', '')
result = 0
for i in number:
    result+=int(i)
    
print (f'Сумма чисел {number} равна {result}')


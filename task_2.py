"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""

seq_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# Вариант 1. С генераторным выражением
seq_list_result1 = [value for index, value in enumerate(seq_list) if
                    index > 0 and seq_list[index] > seq_list[index - 1]]

# Вариант 2. Без генераторного выражения
seq_list_result2 = []
for index, value in enumerate(seq_list):
    if index > 0 and seq_list[index] > seq_list[index - 1]:
        seq_list_result2.append(value)

print(seq_list_result1)
print(seq_list_result2)

"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, hours_in, rate_in, bonus_in = argv


def salary_calc(hours, rate, bonus):
    """
    Функция расчета заработанной платы
    :param hours: отработанные часы
    :param rate: ставка
    :param bonus: премия
    :return: возвращает расчитанную заработанную плату
    """
    try:
        if float(hours) < 0 or float(rate) < 0 or float(bonus) < 0:
            print('Все введенные значения не должны быть отрицательными')
            return

        return (float(hours) * float(rate)) + float(bonus)
    except ValueError:
        print('Ошибка. Все введенные значения должны быть цифрами')


salary = salary_calc(hours_in, rate_in, bonus_in)
print(f"Заработная плата = {salary}") if salary else print(f"Расчет не выполнен")

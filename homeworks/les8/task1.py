'''1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать
два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
@staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.'''
class Date:
    date=input('Ввод даты: ')
    @classmethod
    def number(cls):
        [day,month,year]=[int(i) for i in cls.date.split('-')]
        return [day,month,year]
    @staticmethod
    def validate():
        return 'ok' if 0<Date.number()[0]<32 else 'not ok', 'ok' if 0<Date.number()[1]<13 else 'not ok'
print(Date.number())
print(Date.validate())
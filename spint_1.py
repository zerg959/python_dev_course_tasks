# Python: Основы ООП
# ---------------------------------------
# Добавьте к классу Contact свойства address и birthday
# Создайте объект mike типа Contact с такими данными:
# имя: Михаил Булгаков
# телефон: 2-03-27
# адрес: Россия, Москва, Большая Пироговская, дом 35б, кв. 6
# день рождения: 15.05.1891
# Создайте объект vlad типа Contact с такими данными:
# имя: Владимир Маяковский
# телефон: 73-88
# адрес: Россия, Москва, Лубянский проезд, д. 3, кв. 12
# день рождения: 19.07.1893
# Вызовите функцию print_contact(), чтобы напечатать на экране свойства созданных объектов
#TASK 1
class Contact:
    def __init__(self, name, phone, address, birthday):
        self.name = name
        self.phone = phone
        self.address = address
        self.birthday = birthday
        # добавьте свойство address
        # добавьте свойство birthday
        print(f"Создаём новый контакт {name}")

mike = Contact(name='Михаил Булгаков',
               phone='2-03-27',
               address='Россия, Москва, Большая Пироговская, дом 35б, кв. 6',
               birthday = '15.05.1891')

vlad = Contact('Владимир Маяковский', '73-88', 'Россия, Москва, Лубянский проезд, д. 3, кв. 12', '19.07.1893')
# здесь создайте объекты mike и vlad

def print_contact():
    print(f"{mike.name} — адрес: {mike.address}, телефон: {mike.phone}, день рождения: {mike.birthday}")
    print(f"{vlad.name} — адрес: {vlad.address}, телефон: {vlad.phone}, день рождения: {vlad.birthday}")

print_contact()

# TASK 2

# В 1927 году Булгаков переехал по новому адресу Россия, Москва, Нащокинский переулок, дом 3, кв. 44, его телефон изменился на К-058-67.
# А Маяковский с Лубянки отправился в свою квартиру по адресу Россия, Москва, Гендриков переулок, дом 15, кв. 5, ему туда можно позвонить по телефону 2-35-71.
# Обратитесь к нужным свойствам объектов mike и vlad и запишите в них новые значения.
# Запустите код и проверьте, что получилось: на экран будут выведены новые данные.

class Contact:
    def __init__(self, name, phone, birthday, address):
        self.name = name
        self.phone = phone
        self.birthday = birthday
        self.address = address
        print(f"Создаём новый контакт {name}")


mike = Contact("Михаил Булгаков", "2-03-27", "15.05.1891", "Россия, Москва, Большая Пироговская, дом 35б, кв. 6")
vlad = Contact("Владимир Маяковский", "73-88", "19.07.1893", "Россия, Москва, Лубянский проезд, д. 3, кв. 12")


def print_contact():
    print(f"{mike.name} — адрес: {mike.address}, телефон: {mike.phone}, день рождения: {mike.birthday}")
    print(f"{vlad.name} — адрес: {vlad.address}, телефон: {vlad.phone}, день рождения: {vlad.birthday}")

mike.address = 'Россия, Москва, Нащокинский переулок, дом 3, кв. 44'
mike.phone = 'К-058-67'
# здесь измените адрес для объекта mike
# здесь измените телефон для объекта mike

vlad.phone = '2-35-71'
vlad.address = 'Россия, Москва, Гендриков переулок, дом 15, кв. 5'
# здесь измените адрес для объекта vlad
# здесь измените телефон для объекта vlad

print_contact()  # выводим данные на экран

# Создание новых типов данных в Python
# TASK 1
# 1.
# В прошлом задании для вывода на экран данных о каждом объекте мы писали отдельный код для каждого объекта. Это громоздко и нерационально, ООП позволяет оптимизировать код.
# В классе Contact создайте метод show_contact(), который будет выводить данные любого объекта типа Contact в том же виде, как сейчас их выводит функция print_contact.
# В теле класса Contact напишите метод show_contact, который в качестве параметра будет принимать переменную self. В теле метода выполните print(), точно такой же, как в функции print_contact, только вместо имени объекта в аргументе укажите self.
# Вызовите метод show_contact для объектов mike и vlad
# Удалите из кода функцию print_contact().
# Запустите код
class Contact:
    def __init__(self, name, phone, birthday, address):
        self.name = name
        self.phone = phone
        self.birthday = birthday
        self.address = address
        print(f"Создаём новый контакт {name}")
    # здесь напишите метод show_contact()
    # он будет очень похож на функцию print_contact()
    def show_contact(self):
        print(f"{self.name} — адрес: {self.address}, телефон: {self.phone}, день рождения: {self.birthday}")



mike = Contact("Михаил Булгаков", "2-03-27", "15.05.1891", "Россия, Москва, Большая Пироговская, дом 35б, кв. 6")
vlad = Contact("Владимир Маяковский", "73-88", "19.07.1893", "Россия, Москва, Лубянский проезд, д. 3, кв. 12")
mike.show_contact()
vlad.show_contact()
# обратитесь к методу show_contact() объекта mike
# и к методу show_contact() объекта vlad

# TASK 2
# 2.
# В прекоде подготовлен класс Planet, он описывает планеты и хранит свойства: name (имя), surface_area (площадь поверхности в км²), average_temp_celsius (средняя температура поверхности планеты по Цельсию), average_temp_fahrenheit (то же по Фаренгейту).
# Конструктор класса принимает на вход три параметра: имя планеты, её радиус в километрах и среднюю температуру на поверхности в градусах Цельсия.
# В конструкторе вычислите площадь поверхности планеты. Для упрощения считайте планеты сферическими.
# Площадь поверхности сферы с радиусом r равна 4 * π * r² . Значение числа π получите так: math.pi (для этого подключите модуль math).
# В конструкторе вычислите температуру поверхности по Фаренгейту.
# Чтобы перевести температуру по Цельсию в шкалу Фаренгейта, нужно умножить значение на 9/5 и прибавить 32.

# импортируйте библиотеку math

import math

class Planet:
    def __init__(self, name, radius, temp_celsius):
        self.name = name
        self.surface_area = 4 * math.pi * radius**2
        self.average_temp_celsius = temp_celsius
        self.average_temp_fahrenheit = temp_celsius * (9/5) + 32

    def show_info(self):
        print(f"Планета {self.name} имеет площадь поверхности {self.surface_area} кв.км.")
        print(f"Средняя температура поверхности планеты: {self.average_temp_fahrenheit}° по Фаренгейту.")


jupiter = Planet('Юпитер', 69911, -108)
jupiter.show_info()
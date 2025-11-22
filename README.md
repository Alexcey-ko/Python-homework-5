# Python-homework-4

Выполнение домашнего задания №5. ООП в Python.

Для запуска не требуется дополнительных сторонних зависимостей.

## 1. Создание класса Student

`src\python-homework-5\hw5_1.py`

Создан класс `Student` с атрибутами `name` и `age` и методами `__init__` `get_info`.

## 2. Расширение класса Student

`src\python-homework-5\hw5-2.py`

Добавлен класс `GraduateStudent` с наследованием от `Student`. Добавлен атрибут `research_topic` и методы `add_publication`, `get_publications`.

## 3. Реализация системы управления студентами

`src\python-homework-5\hw5-3.py`

Реализованы магические методы `__str__`, `__repr__` в классе `Student`, магические метод `__repr__` в классе `GraduateStudent`. Магические методы `__getitem__`, `__len__` в классе `StudentManager`. В классе `StudentManager` реализован метод `print_all_info`, который с помощью полиморфизма выводит информацию о студентах.

"""1. ДЗ по ООП. Создание класса Student"""

class Student:
    """Класс студента с базовыми характеристиками"""

    def __init__(self, name:str, age:int):
        """
        Args:
            name (str): Имя студента
            age (int):  Возраст студента
        """
        self.name = name
        self._age = age

    def get_info(self)->str:
        """Возвращает строку с информацией о студенте.

        Returns:
            str: Информация о студенте
        """
        return f'Студент {self.name}, возраст {self._age}'
    
#Инициализация объекта Student
student1 = Student('Анна', 20)
print(student1.get_info())
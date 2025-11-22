"""2. ДЗ по ООП. Расширение класса Student."""

class Student:
    """Класс студента с базовыми характеристиками."""

    def __init__(self, name:str, age:int):
        """Инициализация объекта студента.

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

class GraduateStudent(Student):
    """Класс магистранта/аспиранта, расширающий класс Student."""

    def __init__(self, name:str, age:int, research_topic:str):
        """Инициализация объекта магистранта/аспиранта.

        Args:
            name (str): Имя студента
            age (int):  Возраст студента
            research_topic (str): тема исследования
        """
        super().__init__(name, age)
        self._research_topic = research_topic
        #Количество публикаций
        self.__publications = 0

    def get_info(self)->str:
        """Возвращает строку с информацией о студенте.

        Returns:
            str: информация о студенте
        """
        #Первый вариант: можно взять возврат из класса предка и дополнить
        return super().get_info() + f', тема: {self._research_topic}'
        #Второй вариант: полностью переписать возврат
        #return f'Студент {self.name}, возраст {self._age}, тема: {self._research_topic}'

    def add_publication(self):
        """Увеличение количества публикаций на 1."""
        self.__publications += 1

    def get_publications(self)->int:
        """Получение количества публикаций.

        Returns:
            int: количество публикаций
        """
        return self.__publications

#Инициализация объекта GraduateStudent
grad_student = GraduateStudent('Петр', 25, 'Искусственный интеллект')
print(grad_student.get_info())

#Проверка количества публикаций
print(grad_student.get_publications())
grad_student.add_publication()
grad_student.add_publication()
print(grad_student.get_publications())
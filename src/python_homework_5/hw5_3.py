"""3. ДЗ по ООП. Реализация системы управления студентами."""

class Student:
    """Класс студента с базовыми характеристиками."""

    def __init__(self, name:str, age:int):
        """Инициализация объекта студента.

        Args:
            name (str): имя студента
            age (int):  Возраст студента.
        """
        self.name = name
        self._age = age

    def __str__(self):
        """Человекочитаемое строковое представление объекта.

        Returns:
            str: информация о студенте в удобной для пользователя форме
        """
        return self.get_info()

    def __repr__(self):
        """Техническое строковое представление объекта для разработчика.

        Returns:
            str: полная информация о студенте для диагностики
        """
        return f'Student(name = {self.name}, age = {self.age})'

    def get_info(self)->str:
        """Возвращает строку с информацией о студенте.

        Returns:
            str: информация о студенте
        """
        return f'Студент {self.name}, возраст {self._age}'


class GraduateStudent(Student):
    """Класс магистранта/аспиранта, расширающий класс Student."""

    def __init__(self, name:str, age:int, research_topic:str):
        """Инициализация объекта магистранта/аспиранта.

        Args:
            name (str): имя студента
            age (int):  возраст студента
            research_topic (str): тема исследования
        """
        super().__init__(name, age)
        self._research_topic = research_topic
        #Количество публикаций
        self.__publications = 0

    def __repr__(self):
        """Техническое строковое представление объекта для разработчика.

        Returns:
            str: полная информация о студенте для диагностики
        """
        return (f'Student(name={self.name}, age={self.age},'
                f'_research_topic={self._research_topic}, __publications={self.__publications})')

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


class StudentManager():
    """Класс системы управления студентами."""

    def __init__(self):
        """Инициализация пустого менеджера студентов."""
        self.student_list = []

    def __getitem__(self, index):
        """Получение студента по индексу.

        Args:
            index (int): индекс студента в списке

        Returns:
            Student: объект студента по указанному индексу
        """
        return self.student_list[index]
    
    def __len__(self):
        """Возвращает количество студентов в менеджере.

        Returns:
            int: количество студентов
        """
        return len(self.student_list)

    def add_student(self, student):
        """Добавление студента в менеджер.

        Args:
            student (Student): объект студента для добавления
        """
        self.student_list.append(student)

    def print_all_info(self):
        """Выводит информацию обо всех студентах в менеджере.

        Используется метод "get_info" каждого студента, поддерживая полиморфизм
        """
        for student in self.student_list:
            print(student.get_info())

# Образец использования:
manager = StudentManager()

student1 = Student('Анна', 20)
student2 = GraduateStudent('Петр', 25, 'AI')

manager.add_student(student1)
manager.add_student(student2)

print(len(manager)) #Должно вывести: 2
print(manager[0])   #Должен вывести первого студента

# Полиморфный метод, который выводит информацию о всех студентах
manager.print_all_info()
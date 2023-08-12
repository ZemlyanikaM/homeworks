import csv
from functools import reduce
from pathlib import Path
from random import randint as rnd


class Validator:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not value.isalpha():
            raise TypeError(f'{value} must contains only letters')
        if not value.istitle():
            raise TypeError(f'{value} must start with a capital letter')


class Student:
    name = Validator()
    patronymic = Validator()
    surname = Validator()
    _lessons = None

    def __init__(self, name: str, patronymic: str, surname: str, cvs_file: Path):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self.lessons = cvs_file

    @property
    def lessons(self):
        return self._lessons

    @lessons.setter
    def lessons(self, cvs_file: Path):
        self._lessons = {"lessons": {}}
        with open(cvs_file, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                self._lessons["lessons"][row[0]] = {"rating": [], "test_rating": [], "test_avg": None}
        self._lessons["avg_rating"] = None
        self._lessons["avg_tests"] = None

    def __call__(self, lesson: str, rating: int, rating_type: str = "lesson"):
        if lesson not in self.lessons["lessons"].keys():
            raise AttributeError(f'There is no {lesson} lesson')
        if rating_type == "lesson":
            if rating < 2 or rating > 5:
                raise ValueError("The rating must be in (2,3,4,5)")
            self.lessons["lessons"][lesson]["rating"].append(rating)
            self.lessons["avg_rating"] = self.get_avg_rating(self.lessons)
        elif rating_type == "test":
            if rating < 0 or rating > 100:
                raise ValueError("The rating must be in (0-100)")
            self.lessons["lessons"][lesson]["test_rating"].append(rating)

            self.lessons["lessons"][lesson]["test_avg"] = \
                reduce(lambda x, y: x + y, self.lessons["lessons"][lesson]["test_rating"]) / \
                len(self.lessons["lessons"][lesson]["test_rating"])
            self.lessons['avg_tests'] = self.get_avg_tests(self.lessons)

    @staticmethod
    def get_avg_rating(lessons: dict) -> float:
        all_ratings = []
        [all_ratings.extend(lessons["lessons"][name]["rating"]) for name in lessons["lessons"]]

        return reduce(lambda x, y: x + y, all_ratings) / len(all_ratings)

    @staticmethod
    def get_avg_tests(lessons: dict) -> float:
        all_ratings = []
        [all_ratings.extend(lessons["lessons"][name]["test_rating"]) for name in lessons["lessons"]]

        return reduce(lambda x, y: x + y, all_ratings) / len(all_ratings)

    def __repr__(self):
        message = f'Student full name = {self.name} {self.patronymic} {self.surname}\n' \
                  f'The average lessons rating  = {self.lessons["avg_rating"]}\n' \
                  f'The average tests rating = {self.lessons["avg_tests"]}\n'
        message += "\nLessons ratings:\n"

        for key, value in self.lessons["lessons"].items():
            message += f'{key} = {value["rating"]}\n'
        message += "\nTests ratings:\n"
        for key, value in self.lessons["lessons"].items():
            message += f'{key} = {value["test_rating"]}, average = {value["test_avg"]}\n'

        return message


if __name__ == '__main__':
    Ivan = Student("Ivan", "Ivanovich", "Ivanov", Path('lessons.csv'))
    for i in range(2, 6):
        Ivan("Python", rnd(2, 5))
        Ivan("C++", rnd(2, 5))
        Ivan("C", rnd(2, 5))
        Ivan("Networks", rnd(2, 5))
        Ivan("Linux", rnd(2, 5))
        Ivan("DataBases", rnd(2, 5))
        Ivan("Python", rnd(0, 100), "test")
        Ivan("C++", rnd(0, 100), "test")
        Ivan("DataBases", rnd(0, 100), "test")
        Ivan("C", rnd(0, 100), "test")
        Ivan("Networks", rnd(0, 100), "test")
        Ivan("Linux", rnd(0, 100), "test")
    print(Ivan)

    # Ivan('AnyCourse', rnd(2, 5))
    # Ivan('DataBases', 8)

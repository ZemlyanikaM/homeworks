# Создайте класс Моя Строка, где:
# будут доступны все возможности str, дополнительно хранятся имя автора строки и время создания (time.time)
import time


class MyString(str):
    """
    If you use this class, it will also show you the creator's name and time of creating the object
    """
    def __new__(cls, text: str, creator: str):
        """Gives extra information about your string"""
        print('New started')
        instance = super().__new__(cls, text)
        instance.creator = creator
        instance.time = time.time()
        return instance

    def __str__(self):
        """
        Shows not only text, but also the creator's name and time of creating
        """
        return f'{super().__str__()} created by: {self.creator} at {self.time}'


if __name__ == '__main__':
    example = MyString('text', 'name')
    example_1 = MyString('text1', 'name1')
    print(example)
    print(example.creator)
    print(example_1)
    print(help(MyString.__new__))

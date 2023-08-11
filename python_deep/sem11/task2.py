# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

class Archive:
    '''
    Archive
    '''
    _instance = None

    def __init__(self, text: str, num: int):
        """
        __init__ doc
        :param text:
        :param num:
        """
        print('__init__')
        self.text = text
        self.num = num

    def __new__(cls, *args, **kwargs):
        """
        __new__ doc
        :param args:
        :param kwargs:
        """
        print('__new__')
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.num_arch = []
            cls._instance.text_arch = []
        else:
            cls._instance.num_arch.append(cls._instance.num)
            cls._instance.text_arch.append(cls._instance.text)
        return cls._instance

    def __str__(self):
        return f'Current text: {self.text} and number: {self.num}\nText archive: {self.text_arch}\nNums archive: {self.num_arch}'

    def __repr__(self):
        return f'Current text: {self.text} and number: {self.num}'


if __name__ == '__main__':
    elem_1 = Archive('text', 1)
    elem_2 = Archive('text', 2)
    elem_3 = Archive('text', 3)
    # print(Archive._instance.num_arch)
    # print(help(Archive.__new__))
    print(elem_3)
    print(repr(elem_2))

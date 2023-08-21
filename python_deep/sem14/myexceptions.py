class MyException(Exception):
    pass


class SizesException(MyException):
    def __str__(self):
        if self.operation == 'add':
            return f"Error! The wrong sizes of matrices. Addition is impossible"
        elif self.operation == 'mul':
            return f"Error! The wrong sizes of matrices. Multiplication is impossible "
        else:
            return f"Error! Matrices have different sizes. Comparison is not possible"

    def __init__(self, operation: str):
        self.operation = operation


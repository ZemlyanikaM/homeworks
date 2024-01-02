"""Calculate and compare the average of two lists"""


class ListComparison:
    """Calculate and compare the average of two lists"""

    def __init__(self, list_0: list[int], list_1: list[int]) -> None:
        self.list_0 = list_0
        self.list_1 = list_1
        self._avg_0 = None
        self._avg_1 = None

    @property
    def avg_0(self) -> float | None:
        """The average of the first list"""
        if self._avg_0 is None and self.list_0:
            self._avg_0 = sum(self.list_0) / len(self.list_0)
        return self._avg_0

    @property
    def avg_1(self) -> float | None:
        """The average of the second list"""
        if self._avg_1 is None and self.list_1:
            self._avg_1 = sum(self.list_1) / len(self.list_1)
        return self._avg_1

    def avg_compare(self) -> str:
        """Compare averages of two lists"""
        if None in (self.avg_0, self.avg_1):
            raise ValueError("Оne of the lists is empty. Сomparison is not possible.")
        if self.avg_0 > self.avg_1:
            return "The first list has a higher average value"
        if self.avg_1 > self.avg_0:
            return "The second list has a higher average value"
        return "The average values of the lists are equals"

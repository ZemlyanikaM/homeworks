import pytest
from lst_avg_comp import ListComparison


@pytest.fixture
def list_0():
    return [0, 1, 2, 3, 4]


@pytest.fixture
def list_1():
    return [5, 6, 7, 8, 9]


@pytest.fixture
def empty_list():
    return []


@pytest.fixture
def comparison_instance_lt(list_0, list_1):
    return ListComparison(list_0, list_1)


@pytest.fixture
def comparison_instance_gt(list_0, list_1):
    return ListComparison(list_1, list_0)


@pytest.fixture
def comparison_instance_eq(list_0):
    return ListComparison(list_0, list(reversed(list_0)))


@pytest.fixture
def comparison_instance_empty(list_0, empty_list):
    return ListComparison(list_0, empty_list)


def test_avg_1(comparison_instance_lt):
    assert comparison_instance_lt.avg_0 == 2, "The average of the first list should be 2"


def test_avg_2(comparison_instance_lt):
    assert comparison_instance_lt.avg_1 == 7, "The average of the second list should be 7"


def test_avg_compare_lt(comparison_instance_lt):
    assert comparison_instance_lt.avg_compare() == "The second list has a higher average value", \
        "Checking the comparison. Average of the second list is greater"


def test_avg_compare_gt(comparison_instance_gt):
    assert comparison_instance_gt.avg_compare() == "The first list has a higher average value", \
        "Checking the comparison. Average of the first list is greater"


def test_avg_compare_eq(comparison_instance_eq):
    assert comparison_instance_eq.avg_compare() == "The average values of the lists are equals", \
        "Checking the comparison. Averages of the both lists are equals"


def test_avg_compare_empty(comparison_instance_empty):
    with pytest.raises(ValueError):
        comparison_instance_empty.avg_compare()


if __name__ == '__main__':
    pytest.main(['-v'])

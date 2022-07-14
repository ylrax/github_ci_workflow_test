import pytest
from src.code import Point, Parent, Child


@pytest.fixture
def point_a():
    return Point(1, 1)

@pytest.fixture
def point_b():
    return Point(3, 2)

@pytest.fixture
def parent_a():
    return Parent(prop1=1, prop2="random text")

@pytest.fixture
def child_a():
    return Child()


def test_string_point(point_a):
    assert str(point_a) == "({0},{1})".format(1, 1)


def test_overload_method(point_a, point_b):
    assert (point_a < point_b) is True


def test_child(child_a):
    assert child_a.myMethod() == 'Calling child method'


def test_parent(parent_a):
    assert parent_a.myMethod() == 'Calling parent method'


def test_inherence(child_a, parent_a):
    assert issubclass(type(child_a), Parent)


@pytest.mark.parametrize("a,b,total", [
    (3, 4, 7),
    (200000, 100000, 300000),
])
def test_method(a, b, total, parent_a, child_a):
    assert parent_a.addition_number_method(a, b) == total
    assert child_a.addition_number_method(a, b) == total

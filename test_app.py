import pytest


def test_dictionary_operations():
    """Test dictionary operations from ex1.py"""
    students = {
        " Alice ": 85,
        " Bob ": 92,
        " Charlie ": 78,
        " Diana ": 88
    }

    # Test get
    assert students.get(" Charlie ") == 78
    assert students.get(" Eve ", 0) == 0

    # Test pop
    students_copy = students.copy()
    removed = students_copy.pop(" Bob ", None)
    assert removed == 92
    assert " Bob " not in students_copy

    # Test keys, values, items
    assert list(students.keys()) == [" Alice ", " Bob ", " Charlie ", " Diana "]
    assert list(students.values()) == [85, 92, 78, 88]


def test_list_operations():
    """Test list operations from ex2.py"""
    languages = [" Python ", " JavaScript ", " SQL "]

    # Test append
    languages.append(" Java ")
    assert " Java " in languages

    # Test extend
    languages.extend([" HTML ", " CSS "])
    assert " HTML " in languages
    assert " CSS " in languages

    # Test sort
    original = languages.copy()
    languages.sort()
    # Sort should work, check that the list is sorted
    assert languages == sorted(original)

    # Test index
    sql_index = languages.index(" SQL ")
    assert sql_index >= 0

    # Test in/not in
    assert " C++ " not in languages

    # Test remove
    languages.remove(" JavaScript ")
    assert " JavaScript " not in languages


def test_set_operations():
    """Test set operations from ex3.py"""
    l1 = {" Python ", " SQL ", " Git ", " Docker "}
    l2 = {" Python ", " HTML ", " CSS ", " Git "}

    # Test add
    l1_copy = l1.copy()
    l1_copy.add(" JavaScript ")
    assert " JavaScript " in l1_copy

    # Test union
    union = l1 | l2
    assert " Python " in union
    assert " HTML " in union
    assert " Docker " in union

    # Test intersection
    intersection = l1 & l2
    assert " Python " in intersection
    assert " Git " in intersection
    assert " Docker " not in intersection

    # Test difference
    difference = l1 - l2
    assert " Docker " in difference
    assert " SQL " in difference
    assert " Python " not in difference

    # Test discard
    l1_copy.discard(" Docker ")
    assert " Docker " not in l1_copy
    l1_copy.discard(" Nonexistent ")  # Should not error


def test_functional_operations():
    """Test functional programming operations from ex4.py"""
    from functools import reduce

    prices = [100, 250, 75, 300]
    discounts = [0.1, 0.2, 0.05, 0.15]

    # Test map
    discounted_prices = list(map(lambda p, d: p * (1 - d), prices, discounts))
    expected = [90.0, 200.0, 71.25, 255.0]
    assert discounted_prices == expected

    # Test filter
    expensive_items = list(filter(lambda price: price > 200, discounted_prices))
    assert expensive_items == [255.0]  # Only one > 200

    # Test reduce
    total_discounted_cost = reduce(lambda acc, price: acc + price, discounted_prices, 0)
    expected_total = sum(expected)
    assert total_discounted_cost == expected_total

    # Test zip
    paired = list(zip(prices, discounts))
    assert paired == [(100, 0.1), (250, 0.2), (75, 0.05), (300, 0.15)]

    # Test enumerate
    enumerated = list(enumerate(prices))
    assert enumerated == [(0, 100), (1, 250), (2, 75), (3, 300)]


def test_stack_operations():
    """Test stack operations from ex5.py"""
    undo_stack = []

    # Test append
    undo_stack.append(" Type 'Hello '")
    undo_stack.append(" Bold ")
    undo_stack.append(" Delete 'o '")
    undo_stack.append(" Undo, Bold ")

    assert len(undo_stack) == 4

    # Test pop
    popped = undo_stack.pop()
    assert popped == " Undo, Bold "
    assert len(undo_stack) == 3

    # Test top action
    assert undo_stack[-1] == " Delete 'o '"

    # Test not empty
    assert undo_stack

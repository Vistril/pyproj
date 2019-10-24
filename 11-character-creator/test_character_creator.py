import pytest
import character_creator as student
dict = {'Strength':10,
        'Dexterity':10,
        'Constitution':10,
        'Wisdom':10,
        'Intelligence':10,
        'Charisma':10,
        'Pool':5}

def test_add1():
    assert student.add('Wisdom', 5, dict) == '5 added to Wisdom'
def test_add2():
    assert student.add('Strength', 6, dict) == '6 is more points than you have left in your pool'
def test_add3():
    assert student.add('Health', 2, dict) == 'Health is not a valid attribute'
def test_remove1():
    assert student.remove('Intelligence', 10, dict) == '10 removed from Intelligence'
def test_remove2():
    assert student.remove('Constitution', 11, dict) == '11 is more points than you have left in Constitution'
def test_remove3():
    assert student.remove('Bob', 2, dict) == 'Bob is not a valid attribute'
def test_remove4():
    assert student.remove('Dexterity', 5, dict) == '5 removed from Dexterity'
def test_add4():
    assert student.add('Charisma', 2, dict) == '2 added to Charisma'

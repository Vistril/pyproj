import pytest
import counter as student

def test1():
    assert student.count(1,10,2) == "1 3 5 7 9 "

def test2():
    assert student.count(0,10,2) == "0 2 4 6 8 10 "

def test3():
    assert student.count(0,10,-1) == ""

def test4():
    assert student.count(10,0,-1) == "10 9 8 7 6 5 4 3 2 1 0 "

def test5():
    assert student.count(0,100,7) == "0 7 14 21 28 35 42 49 56 63 70 77 84 91 98 "

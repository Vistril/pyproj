import pytest
import pig_latin as student

def test1():
    assert student.ay_end("speaker",2)=="eakerspay "
def test2():
    assert student.ay_end("Happy!",1)=="appyHay! "
def test3():
    assert student.way_end("eggs")=="eggsway "
def test4():
    assert student.way_end("Apple!")=="Appleway! "
def test5():
    assert student.translator("This, a Message, is.")=="isthay, away essagemay, isway. "

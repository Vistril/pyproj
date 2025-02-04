import pytest, os, pickle
import TC2 as student

def test_next_block1():
    f = open('test.txt','w')
    rep = "category\nquestion\na1\na2\na3\na4\n1\nexplanation\n1\n"
    f.write(rep)
    f.close()
    f = open('test.txt','r')
    assert student.next_block(f) == ("category\n","question\n",["a1\n","a2\n","a3\n","a4\n"],"1","explanation\n",1)
    f.close()
    os.remove('test.txt')
def test_next_block2():
    f = open('test.txt','w')
    rep = "category\nquestion\na1\na2\na3\na4\n1\nexplanation\n14\n"
    f.write(rep)
    f.close()
    f = open('test.txt','r')
    assert student.next_block(f) == ("category\n","question\n",["a1\n","a2\n","a3\n","a4\n"],"1","explanation\n",14)
    f.close()
    os.remove('test.txt')
def test_next_block3():
    f = open('test.txt','w')
    rep = "category\nquestion\na1\na2\na3\na4\n1\nexplanation\n140\n"
    f.write(rep)
    f.close()
    f = open('test.txt','r')
    assert student.next_block(f) == ("category\n","question\n",["a1\n","a2\n","a3\n","a4\n"],"1","explanation\n",140)
    f.close()
    os.remove('test.txt')

def test_sortNsave1():
    hs = [(2,'DEF'),(1,'GHI'),(0,'ABC')]
    hs = student.sortNsave(3,'ABC',hs)
    f = open('highscores.dat',"rb")
    hs1 = pickle.load(f)
    f.close()
    assert hs1 == hs and hs == [(3,'ABC'),(2,'DEF'),(1,'GHI')]
def test_sortNsave2():
    hs = [(20,'DEF'),(10,'GHI'),(15,'ABC')]
    hs = student.sortNsave(3,'NEW',hs)
    f = open('highscores.dat',"rb")
    hs1 = pickle.load(f)
    f.close()
    assert hs1 == hs and hs == [(20,'DEF'),(15,'ABC'),(10,'GHI')]
def test_sortNsave3():
    hs = [(20,'DEF'),(10,'GHI'),(15,'ABC')]
    hs = student.sortNsave(30,'NEW',hs)
    f = open('highscores.dat',"rb")
    hs1 = pickle.load(f)
    f.close()
    assert hs1 == hs and hs == [(30,'NEW'),(20,'DEF'),(15,'ABC')]

def test_hs_table1():
    hs = [(20,'DEF'),(10,'GHI'),(15,'ABC')]
    assert student.hs_table(hs) == 'Name: DEF\tScore: 20\nName: GHI\tScore: 10\nName: ABC\tScore: 15\n'
def test_hs_table2():
    hs = [(2,'DEF'),(1,'GHI'),(0,'ABC')]
    assert student.hs_table(hs) == 'Name: DEF\tScore: 2\nName: GHI\tScore: 1\nName: ABC\tScore: 0\n'
def test_hs_table3():
    hs = [(2,'DEF'),(1,'GHI'),(0,'ABC'),(20,'DEF'),(10,'GHI'),(15,'ABC')]
    assert student.hs_table(hs) == 'Name: DEF\tScore: 2\nName: GHI\tScore: 1\nName: ABC\tScore: 0\nName: DEF\tScore: 20\nName: GHI\tScore: 10\nName: ABC\tScore: 15\n'

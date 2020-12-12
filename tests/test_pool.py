import unittest
from elegant_structure import Pool

class Test:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class TestPool(unittest.TestCase):

  def test_add(self):
    pool = Pool(Test)
    x = pool.add(1, 2)
    y = pool.add(3, 4)
    self.assertEqual(x, 0)
    self.assertEqual(y, 1)
    
  def test_remove(self):
    pool = Pool(Test)
    x = pool.add(1, 2)
    y = pool.add(3, 4)
    pool.remove(x)
    self.assertEqual(pool[x], None)
    pool.remove(y)
    self.assertEqual(pool[y], None)
    
  def test_all(self):
    pool = Pool(Test)
    x = pool.add(1, 2)
    y = pool.add(3, 4)
    self.assertEqual(len(pool.all()), 2)
    pool.remove(x)
    self.assertEqual(len(pool.all()), 1)
    
  def test_get(self):
    pool = Pool(Test)
    x = pool.add(1, 2)
    y = pool.add(3, 4)
    pool.remove(x)
    self.assertEqual(pool[x], None)
    self.assertEqual(pool[y].x, 3)
    self.assertEqual(pool[y].y, 4)
    
if __name__ == '__main__':
    unittest.main()

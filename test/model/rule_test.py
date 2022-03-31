import unittest

from lsystem.model.rule import Rule
from lsystem.model.symbol import Symbol




class TestModelRule(unittest.TestCase):
    """ Test grammar rule. """
    
    
    def setUp(self) -> None:
        
        self.l1 = Symbol('A')
        self.r1 = [Symbol(x) for x in ['A','B','A']]
        self.rule1 = Rule(self.l1, self.r1)
        
        self.l2 = Symbol('A')
        self.r2 = [Symbol(x) for x in ['A','B','A']]
        self.rule2 = Rule(self.l2, self.r2)
        
        self.l3 = Symbol('B')
        self.r3 = [Symbol(x) for x in ['B','A','B']]
        self.rule3 = Rule(self.l3, self.r3)
        

    
    def test_constructor(self):
        
        self.assertRaises(TypeError, Rule, (None, None))
        self.assertRaises(TypeError, Rule, (self.l1, 1))
        self.assertRaises(TypeError, Rule, ('A', self.r1))
    
    
    
    def test_equals(self):
        
        self.assertEqual(self.rule1, self.rule2)
        self.assertNotEqual(self.rule1, self.rule3)
        self.assertNotEqual(self.rule2, self.rule3)
        
        
        
    def test_applicable(self):
        
        self.assertTrue(self.rule1.is_applicable(self.l1))
        self.assertFalse(self.rule3.is_applicable(self.l1))
        self.assertTrue(self.rule3.is_applicable(self.l3))
        
        
        
    def test_representation(self):
        
        s = 'A -> ABA'
        self.assertEqual(s, str(self.rule1))
        
        

if __name__ == "__main__":
    unittest.main()        
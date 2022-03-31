import unittest

from lsystem.model.rule import Rule
from lsystem.model.symbol import Symbol




class TestModelSymbol(unittest.TestCase):
    """ Test grammar symbol. """
    
    
    def setUp(self) -> None:
        
        self.s1 = Symbol('A')
        self.s2 = Symbol('A')
        
        self.s3 = Symbol('B')
        self.s4 = Symbol('ABC')
        
        self.rule1 = Rule(self.s3, [self.s4])
        self.rule2 = Rule(self.s2, [self.s1, self.s3, self.s1])
    

    
    def test_constructor(self):
        
        s = Symbol('A')
        self.assertEqual(s.value, 'A')
    
        self.assertRaises(ValueError, Symbol, (1))
        self.assertRaises(ValueError, Symbol, (0.25))
        self.assertRaises(ValueError, Symbol, (Rule))
    
    
    
    def test_equals(self):
        
        self.assertEqual(self.s1, self.s2)
        self.assertNotEqual(self.s1, self.s3)
        
        
        
    def test_apply_rule(self):
        
        self.assertRaises(ValueError, self.s1.apply_rule, (self.rule1))
        
        self.assertEqual(self.s4, *self.s3.apply_rule(self.rule1))
        
        result = [Symbol(x) for x in 'ABA']
        self.assertEqual(result, self.s1.apply_rule(self.rule2))
        


    def test_representation(self):
        
        self.assertEqual(str(self.s1), 'A')
        self.assertEqual(str(self.s4), 'ABC')



if __name__ == "__main__":
    unittest.main()        
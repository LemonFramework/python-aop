import unittest
from aop import AspectType


class TestAspectType(unittest.TestCase):
    def test_pointcut_attr(self):
        class TestClass(metaclass=AspectType):
            pass
        
        self.assertTrue(hasattr(TestClass, 'pointcut'))
    
    def test_pointcut(self):
        class TestClass(metaclass=AspectType):
            def method(self):
                return True
        
        class MockAspect(object):
            def __init__(self, *args, **kwargs):
                pass
            
            def __call__(self, *args, **kwargs):
                return None
        
        TestClass.pointcut('method', MockAspect)
        
        t = TestClass()
        
        self.assertIsNone(t.method())


if __name__ == '__main__':
    unittest.main()

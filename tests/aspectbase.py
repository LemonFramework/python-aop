import unittest
from aop import Aspect


class TestAspect(unittest.TestCase):
    def test_call(self):
        def always_true():
            return True
        
        always_true = Aspect(always_true)
        
        self.assertTrue(always_true())
    
    def test_execute(self):
        def always_true():
            return True
        
        class ExecuteReturnsFalse(Aspect):
            def execute(self, *args, **kwargs):
                return False
        
        always_true = ExecuteReturnsFalse(always_true)
        
        self.assertFalse(always_true())
    
    def test_around(self):
        def always_true():
            return True
        
        class AroundReturnsFalse(Aspect):
            def around(self, *args, **kwargs):
                return False
        
        always_true = AroundReturnsFalse(always_true)
        
        self.assertFalse(always_true())
    
    def test_exception(self):
        class CustomException(Exception):
            pass
        
        def raise_exception():
            raise CustomException()
        
        raise_exception = Aspect(raise_exception)
        
        with self.assertRaises(CustomException):
            raise_exception()
    
    def test_catch_exception(self):
        def raise_exception():
            raise Exception()
        
        class CatchException(Aspect):
            def exception(self, *args, **kwargs):
                return None
        
        raise_exception = CatchException(raise_exception)
        
        self.assertIsNone(raise_exception())
    
    def test_before_raises_exception(self):
        class BeforeException(Exception):
            pass
        
        def always_true():
            return True
        
        class AspectBeforeException(Aspect):
            def before(self, *args, **kwargs):
                raise BeforeException()
        
        always_true = AspectBeforeException(always_true)
        
        with self.assertRaises(BeforeException):
            always_true()
    
    def test_after_raises_exception(self):
        class AfterException(Exception):
            pass
        
        def always_true():
            return True
        
        class AspectBeforeException(Aspect):
            def after(self, *args, **kwargs):
                raise AfterException()
        
        always_true = AspectBeforeException(always_true)
        
        with self.assertRaises(AfterException):
            always_true()


if __name__ == '__main__':
    unittest.main()

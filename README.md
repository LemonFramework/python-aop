Python AOP Framework
====================

Examples
--------

### Definition of Aspects ###

	>>> import logging
	>>> from aop import Aspect
	>>> 
	>>> class InvocationLoggerAspect(Aspect):
	...     def __init__(self, *args, **kwargs):
	...         super().__init__(*args, **kwargs)
	...         self.logger = logging.getLogger('python-aop')
	...         self.logger.setLevel(logging.DEBUG)
	...     
	...         fh = logging.FileHandler('auth.log')
	...         fh.setLevel(logging.DEBUG)
	...     
	...         self.logger.addHandler(fh)
	...     
	...     def before(self, *args, **kwargs):
	...         self.logger.info(
	...             'Invocation: name=%s, args=%s, kwargs=%s' % (
	...                 self.function,
	...                 args,
	...                 kwargs
	...             )
	...         )
	... 
	>>> 


### Use of Aspect over functions ###

If we want to log each invocation attempt we can apply the aspect directly to a function

	>>> def auth(user, password):
	...     if user is 'aop' and password is '#$%3&23%#$(%':
	...         return True
	...     return False
	... 
	>>> 
	>>> auth = InvocationLoggerAspect(auth)
	>>> 
	>>> auth('aop', '#$%3&23%#$(%')
	True
	>>> auth('aop', '')
	False
	>>>

The content of **auth.log**:

	Invocation: name=<function auth at 0x7f1e30282290>, args=('aop', '#$%3&23%#$(%'), kwargs={}
	Invocation: name=<function auth at 0x7f1e30282290>, args=('aop', ''), kwargs={}

Python AOP Framework
====================

Examples
--------

### Definition of Aspects ###

	>>> class LogAspect(Aspect):
	...     def before(self, *args, **kwargs):
	...         print('Autentication logged:', self.function.__name__, args, kwargs)

### Use of Aspect over functions ###

	>>> from aop import Aspect
	>>> class LogAspect(Aspect):
	...     def before(self, *args, **kwargs):
	...         print('Autentication logged:', self.function.__name__, args, kwargs)
	... 
	>>> def auth(user, password):
	...     # ...
	...     pass
	... 
	>>> auth = LogAspect(auth)
	>>> auth('aop', '#$%3&23%#$(%')
	Autentication logged: auth ('aop', '#$%3&23%#$(%') {}
	>>>

